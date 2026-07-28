# -*- coding: utf-8 -*-
"""
build_base.py — Andamiaje comun de los scripts de carga (builds).

Factoriza la plomeria que hasta ahora se repetia en cada build_*.py:
apertura del CSV del modulo, calculo del Trip_ID inicial, funcion add() y volcado final.
Asi cada build queda reducido a LOS DATOS de los viajes, que es lo unico propio de cada bloque.

USO TIPICO:

    from build_base import Bloque

    b = Bloque("uruguay", president="Yamandú Orsi", origin="Uruguay", modo="append")

    b.add("URU-YO-J001", Trip_Status="Completed", Start_Date="2025-04-07", ...)
    b.add("URU-YO-J001", Trip_Status="Completed", Start_Date="2025-04-08", ...)

    b.guardar()

REGLAS QUE RESPETA (heredadas del proyecto):
- Trip_ID secuencial: arranca en 1 si el modulo es nuevo, o continua el maximo existente.
  (Recordar: integrate.py REASIGNA Trip_ID globalmente; el identificador estable
   cross-file es (Journey_ID, Destination_City), nunca Trip_ID.)
- new_row() completa NA por defecto y auto-deriva Verificacion_Status
  (http -> Verificada-URL; si no -> Solo-Query). Se puede forzar con vs=...
- Las filas de una misma gira multi-pais comparten Journey_ID.
"""
import csv, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(ROOT, "03_MODULOS_PAIS")


class Bloque:
    """Acumula las filas de un bloque (un mandatario o una tanda) y las vuelca al CSV del modulo."""

    def __init__(self, pais, president=None, origin=None, modo="append", trip_id_inicial=None):
        """
        pais    : carpeta del modulo ('argentina', 'brasil', 'chile', 'uruguay', ...)
        president / origin : valores por defecto de esas columnas (se pueden pisar por fila)
        modo    : 'append' anexa al CSV existente | 'create' crea el CSV con encabezado
        trip_id_inicial : fuerza el Trip_ID de arranque (si no, se calcula solo)
        """
        self.pais = pais
        self.president = president
        self.origin = origin
        self.modo = modo
        self.path = os.path.join(MOD, pais, f"{pais}_viajes.csv")
        self.rows = []
        self.tid = trip_id_inicial if trip_id_inicial is not None else self._siguiente_tid()

    def _siguiente_tid(self):
        """Trip_ID inicial: 1 si el modulo no existe/esta vacio; si no, el maximo + 1."""
        if not os.path.exists(self.path):
            return 1
        filas = list(csv.DictReader(open(self.path, encoding="utf-8")))
        return max((int(r["Trip_ID"]) for r in filas), default=0) + 1

    def add(self, journey_id, vs=None, **kw):
        """Agrega una fila. vs fuerza Verificacion_Status (No-verificable / Solo-Query / Verificada-URL)."""
        if self.president: kw.setdefault("President", self.president)
        if self.origin:    kw.setdefault("Origin_Country", self.origin)
        kw["Journey_ID"] = journey_id
        kw["Trip_ID"] = self.tid
        fila = new_row(**kw)
        if vs:
            fila["Verificacion_Status"] = vs
        self.rows.append(fila)
        self.tid += 1
        return fila

    def guardar(self, verbose=True):
        """Vuelca las filas al CSV del modulo segun el modo elegido."""
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        nuevo = (self.modo == "create") or not os.path.exists(self.path)
        with open(self.path, "w" if nuevo else "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if nuevo:
                w.writeheader()
            for r in self.rows:
                w.writerow({c: r.get(c, "NA") for c in COLUMNS})
        if verbose:
            quien = self.president or self.pais
            print(f"OK: {len(self.rows)} filas de {quien} -> {os.path.basename(self.path)} "
                  f"(Trip_ID hasta {self.tid - 1})")
        return len(self.rows)

    # --- utilidades de control ---
    def resumen(self):
        """Chequeo rapido antes de guardar: cuantas filas, cuantos viajes fisicos, cuantos cancelados."""
        journeys = {r["Journey_ID"] for r in self.rows}
        canc = sum(1 for r in self.rows if r.get("Trip_Status") == "Canceled")
        return {"filas": len(self.rows), "viajes": len(journeys), "cancelados": canc}
