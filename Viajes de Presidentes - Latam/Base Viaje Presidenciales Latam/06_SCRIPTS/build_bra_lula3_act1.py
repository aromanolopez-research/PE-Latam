# -*- coding: utf-8 -*-
"""
BRASIL — Lula III, ACTUALIZACION INCREMENTAL 1 (2026-07-07). Corte de base extendido a 2026-07-07.
Diff contra lo cargado: ultima fila previa = IV Cupula CELAC-UE Colombia (J203, 9-10/11/2025).
Research 2026-07-07 (busqueda web activa): 4 giras / 7 filas pais entre abril y junio 2026, incluido el
HALLAZGO de la re-verificacion: reunion con Trump en Washington (6-8/5/2026, ~3 horas, tarifaço/Pix/
minerales criticos). Journeys BRA-LU3-J204..J207; Trip_ID 272-278 (continua max del modulo=271).
Perfil: anio electoral (1ra vuelta oct-2026) -> agenda reducida y economica; sin viajes tras el 30/6
por restriccion electoral vigente desde el 4/7.
BRECHA DETECTADA Y NO CARGADA: dic-2025 a mar-2026 sin cobertura verificada — registrada en
PENDIENTES para investigacion complementaria (anti-alucinacion: nada sin fuente).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "brasil", "brasil_viajes.csv")
P = "Luiz Inácio Lula da Silva"; O = "Brasil"
rows = []; tid = 272

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# Gira Europa (Espania-Alemania-Portugal), J204
add("BRA-LU3-J204", Trip_Status="Completed", Start_Date="2026-04-16", End_Date="2026-04-18", Duration_Days=3,
    Destination_Country="Spain", Destination_City="Barcelona", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="I Cumbre Brasil-España + IV Foro Democracia Sempre",
    Trip_Objective="Firma de acuerdos bilaterales; defensa de la democracia y del multilateralismo junto a Sanchez, Sheinbaum, Petro, Orsi y Ramaphosa.",
    Source_Verification="https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/declaracao-conjunta-por-ocasiao-da-i-cupula-espanha-brasil-barcelona-17-de-abril-de-2026",
    Source_Reliability="High", Methodological_Notes="Evento primario: Foro Democracia Sempre (multilateral); cumbre bilateral al margen. Llego la noche del 16/4.",
    Tema_Foro="Cooperación Política General")

add("BRA-LU3-J204", Trip_Status="Completed", Start_Date="2026-04-19", End_Date="2026-04-20", Duration_Days=2,
    Destination_Country="Germany", Destination_City="Hannover", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Friedrich Merz / Hannover Messe 2026",
    Trip_Objective="Visita de Estado; honores del canciller Merz; ~10 acuerdos (defensa, IA, clima, minerales criticos); Brasil pais socio de la feria.",
    Source_Verification="https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/atos-adotados-por-ocasiao-da-visita-de-estado-do-presidente-luiz-inacio-lula-da-silva-a-hannover-alemanha-19-e-20-de-abril-de-2026-2",
    Source_Reliability="High", Methodological_Notes="3a Consulta Intergubernamental Brasil-Alemania.")

add("BRA-LU3-J204", Trip_Status="Completed", Start_Date="2026-04-21", End_Date="2026-04-21", Duration_Days=1,
    Destination_Country="Portugal", Destination_City="Lisboa", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="PM Luís Montenegro / presidente António José Seguro",
    Trip_Objective="Cierre de gira europea; cooperacion bilateral con foco en la comunidad brasilenia y la CPLP.",
    Source_Verification="https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2026/04/presidente-lula-cumpre-agenda-na-espanha-alemanha-e-portugal-entre-17-e-21-de-abril",
    Source_Reliability="High", Methodological_Notes="NA")

# Washington (hallazgo de re-verificacion), J205
add("BRA-LU3-J205", Trip_Status="Completed", Start_Date="2026-05-06", End_Date="2026-05-08", Duration_Days=3,
    Destination_Country="United States", Destination_City="Washington DC", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Donald Trump",
    Trip_Objective="Reunion de casi tres horas en la Casa Blanca (7/5): tarifaço, Seccion 301/Pix, crimen organizado, minerales criticos, reforma de la ONU.",
    Source_Verification="https://agenciabrasil.ebc.com.br/internacional/noticia/2026-05/lula-deixa-a-casa-branca-apos-reuniao-com-trump",
    Source_Reliability="High", Methodological_Notes="HALLAZGO de re-verificacion 2026-07-07 (no estaba en la base): Agencia Brasil + Poder360 + La Nacion.")

# Suiza + G7 Evian, J206
add("BRA-LU3-J206", Trip_Status="Completed", Start_Date="2026-06-15", End_Date="2026-06-15", Duration_Days=1,
    Destination_Country="Switzerland", Destination_City="Geneva", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Guy Parmelin",
    Trip_Objective="Bilateral con el presidente suizo sobre comercio y Acuerdo MERCOSUR-EFTA, al llegar a Ginebra rumbo al G7.",
    Source_Verification="https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/notas-oficiais/notas-a-imprensa/lula-tem-reuniao-bilateral-com-o-presidente-da-suica-guy-parmelin",
    Source_Reliability="High", Methodological_Notes="Visita bilateral real (nota oficial Planalto), no escala tecnica. Mismo Journey que el G7 (J206).")

add("BRA-LU3-J206", Trip_Status="Completed", Start_Date="2026-06-15", End_Date="2026-06-17", Duration_Days=3,
    Destination_Country="France", Destination_City="Évian-les-Bains", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G7 de Évian (invitado)",
    Trip_Objective="Decima participacion en el G7; parcerias internacionales, crecimiento e IA; bilaterales con Macron y la PM japonesa Takaichi.",
    Source_Verification="https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/participacao-do-presidente-luiz-inacio-lula-da-silva-na-cupula-do-g7-em-evian-les-bains-franca-2013-16-e-17-de-junho-de-2026",
    Source_Reliability="High", Methodological_Notes="Tema G7 -> Cooperacion Politica General (doctrina 5.7).",
    Tema_Foro="Cooperación Política General")

# Cumbre MERCOSUR Asuncion, J207
add("BRA-LU3-J207", Trip_Status="Completed", Start_Date="2026-06-30", End_Date="2026-06-30", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="LXVIII Cúpula do MERCOSUL",
    Trip_Objective="Defensa del MERCOSUR como necesidad estrategica; aporte de USD 100 millones al FOCEM; bilateral con Kast.",
    Source_Verification="https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2026/06/presidente-lula-participa-da-lxviii-cupula-do-mercosul-no-paraguai-em-30-de-junho",
    Source_Reliability="High", Methodological_Notes="Viaje de un dia. Ultimo viaje previsto del semestre: restriccion electoral desde el 4/7.",
    Tema_Foro="Comercio/Integración Económica")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} (actualizacion 2026-07-07) agregadas. Ultimo Trip_ID = {tid-1}")
