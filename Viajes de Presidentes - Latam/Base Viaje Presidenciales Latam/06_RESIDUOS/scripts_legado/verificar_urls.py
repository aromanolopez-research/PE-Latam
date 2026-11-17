# -*- coding: utf-8 -*-
"""
verificar_urls.py — Auditoria de las fuentes de la base.

DOS MODOS:

  1) INVENTARIO (offline, no necesita red) — funciona siempre:
        python3 06_SCRIPTS/verificar_urls.py inventario
     Extrae todas las URLs, detecta malformadas, lista dominios mas usados,
     cuenta filas sin URL y cruza con Verificacion_Status para detectar inconsistencias.

  2) CHEQUEO (necesita conexion a internet) — correr desde una maquina con red:
        python3 06_SCRIPTS/verificar_urls.py chequear
        python3 06_SCRIPTS/verificar_urls.py chequear --limite 50
     Hace un HEAD/GET a cada URL unica y reporta responde / 404 / timeout / error.
     Escribe el resultado en 05_BITACORA/reporte_urls.csv para trabajar sobre el.

Objetivo: convertir la campaña de verificacion (hoy artesanal) en algo semi-automatico.
NO modifica la base: solo audita y reporta.
"""
import csv, os, re, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "04_BASE_FINAL", "base_consolidada.csv")
SALIDA = os.path.join(ROOT, "05_BITACORA", "reporte_urls.csv")

URL_RE = re.compile(r'https?://[^\s<>"\')]+')


def cargar():
    if not os.path.exists(BASE):
        sys.exit(f"No se encontro la base en {BASE}")
    return list(csv.DictReader(open(BASE, encoding="utf-8")))


def extraer_urls(rows):
    """Devuelve {url: [(Journey_ID, Destination_City, President), ...]}"""
    idx = defaultdict(list)
    for r in rows:
        for u in URL_RE.findall(r.get("Source_Verification", "") or ""):
            idx[u.rstrip(".,;)")].append(
                (r["Journey_ID"], r["Destination_City"], r["President"]))
    return idx


def inventario(rows):
    idx = extraer_urls(rows)
    con_url = sum(1 for r in rows if URL_RE.search(r.get("Source_Verification", "") or ""))
    con_query = sum(1 for r in rows if (r.get("Source_Verification", "") or "").startswith("Search Query"))
    print("=" * 60)
    print("INVENTARIO DE FUENTES")
    print("=" * 60)
    print(f"Filas totales           : {len(rows)}")
    print(f"Filas con URL           : {con_url}")
    print(f"Filas con Search Query  : {con_query}")
    print(f"Filas sin ninguna fuente: {len(rows) - con_url - con_query}")
    print(f"URLs unicas             : {len(idx)}")
    print()

    print("--- Dominios mas usados (top 15) ---")
    dom = Counter()
    for u in idx:
        m = re.match(r'https?://([^/]+)', u)
        if m:
            dom[m.group(1).replace("www.", "")] += len(idx[u])
    for d, n in dom.most_common(15):
        print(f"  {n:>4}  {d}")
    print()

    # URLs sospechosas de estar malformadas
    # Ojo: las URLs de Wayback contienen dos "http" por disenio, no son malformadas.
    raras = [u for u in idx
             if " " in u or len(u) < 15
             or (u.count("http") > 1 and "web.archive.org" not in u)]
    print(f"--- URLs sospechosas de malformacion: {len(raras)} ---")
    for u in raras[:10]:
        print(f"  {u}")
    print()

    # Inconsistencias entre Source_Verification y Verificacion_Status
    inc = []
    for r in rows:
        sv = r.get("Source_Verification", "") or ""
        vs = r.get("Verificacion_Status", "") or ""
        tiene_url = bool(URL_RE.search(sv))
        if tiene_url and vs == "Solo-Query":
            # OJO: puede ser INTENCIONAL. El proyecto marca Solo-Query a filas que
            # tienen URL pero cuya evidencia es debil (nota previa al evento,
            # fuente de planificacion, mencion indirecta). Revisar caso por caso
            # antes de "corregir": no todo lo que figura aca es un error.
            inc.append((r["Journey_ID"], r["Destination_City"],
                        "tiene URL pero figura Solo-Query (puede ser intencional: fuente debil)"))
        if not tiene_url and vs == "Verificada-URL":
            inc.append((r["Journey_ID"], r["Destination_City"], "sin URL pero figura Verificada-URL"))
    print(f"--- Inconsistencias Source_Verification vs Verificacion_Status: {len(inc)} ---")
    for j, c, msg in inc[:15]:
        print(f"  {j:<18} {c[:20]:<20} {msg}")
    if len(inc) > 15:
        print(f"  ... y {len(inc)-15} mas")
    print()

    # Prioridad de trabajo: Solo-Query agrupadas por presidente
    sq = [r for r in rows if r.get("Verificacion_Status") == "Solo-Query"]
    print(f"--- Pendientes de verificar (Solo-Query): {len(sq)} ---")
    print("    Top presidentes con mas filas pendientes:")
    for p, n in Counter(r["President"] for r in sq).most_common(10):
        print(f"  {n:>4}  {p}")
    return idx


def chequear(rows, limite=None):
    try:
        import urllib.request, urllib.error, socket
    except ImportError:
        sys.exit("urllib no disponible")
    idx = extraer_urls(rows)
    urls = sorted(idx)
    if limite:
        urls = urls[:limite]
    print(f"Chequeando {len(urls)} URLs unicas (puede tardar)...")
    res = []
    for i, u in enumerate(urls, 1):
        estado = "?"
        try:
            req = urllib.request.Request(u, method="HEAD",
                                         headers={"User-Agent": "Mozilla/5.0 (verificacion academica)"})
            with urllib.request.urlopen(req, timeout=12) as r:
                estado = f"OK-{r.status}"
        except urllib.error.HTTPError as e:
            estado = f"HTTP-{e.code}"
        except (urllib.error.URLError, socket.timeout):
            estado = "TIMEOUT/URLERROR"
        except Exception as e:
            estado = f"ERROR-{type(e).__name__}"
        res.append((u, estado, len(idx[u])))
        if i % 25 == 0:
            print(f"  ... {i}/{len(urls)}")
    with open(SALIDA, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["URL", "Estado", "Filas_que_la_usan"])
        w.writerows(res)
    print()
    print("--- Resumen ---")
    for e, n in Counter(e for _, e, _ in res).most_common():
        print(f"  {n:>4}  {e}")
    print(f"\nReporte guardado en: {SALIDA}")
    caidas = [(u, n) for u, e, n in res if not e.startswith("OK")]
    if caidas:
        print(f"\nURLs con problema ({len(caidas)}), ordenadas por impacto:")
        for u, n in sorted(caidas, key=lambda x: -x[1])[:20]:
            print(f"  [{n} filas] {u}")


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "inventario"
    rows = cargar()
    if modo == "inventario":
        inventario(rows)
    elif modo == "chequear":
        lim = None
        if "--limite" in sys.argv:
            lim = int(sys.argv[sys.argv.index("--limite") + 1])
        chequear(rows, lim)
    else:
        sys.exit("Modo invalido. Usar: inventario | chequear")
