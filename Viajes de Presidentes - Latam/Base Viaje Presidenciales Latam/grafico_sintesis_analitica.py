# -*- coding: utf-8 -*-
"""
grafico_sintesis_analitica.py — Figura de sintesis (2026-07-07).
Tablero de 4 paneles con los hallazgos centrales de la base (v1.4, corte 2026-07-07):
 A) Latido temporal: tramos completados por anio y categoria (shock COVID 2020).
 B) Geografia invertida: bilateral vs multilateral por destino.
 C) Olas regionales: heatmap anio x region de destino.
 D) Perfiles presidenciales: intensidad (viajes/anio) vs vocacion multilateral (%).
Unidad: tramos pais-visita completados (A-C); viajes fisicos completados/anio (D).
"""
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as mticker

plt.style.use('seaborn-v0_8-whitegrid')

rows = list(csv.DictReader(open('04_BASE_FINAL/base_consolidada.csv', encoding='utf-8')))
df = pd.DataFrame(rows)
df = df[df['Trip_Status'] == 'Completed'].copy()
df['Anio'] = df['Start_Date'].str[:4].astype(int)
df['Prefijo'] = df['Journey_ID'].str.rsplit('-J', n=1).str[0]
ANIOS = list(range(2000, 2027))
C_BI, C_MU = '#0173B2', '#DE8F05'
C_PAIS = {'Argentina': '#56B4E9', 'Brasil': '#009E73', 'Chile': '#D55E00'}

fig = plt.figure(figsize=(15.5, 12))
gs = gridspec.GridSpec(2, 2, hspace=0.34, wspace=0.22)

# ── A) Latido temporal ─────────────────────────────────────────────────────
axA = fig.add_subplot(gs[0, 0])
for cat, color in [('Bilateral', C_BI), ('Multilateral', C_MU)]:
    s = df[df['Visit_Category'] == cat].groupby('Anio').size().reindex(ANIOS, fill_value=0)
    axA.plot(s.index, s.values, marker='o', ms=4, lw=1.8, color=color, label=cat)
tot2020 = int(df[df['Anio'] == 2020].groupby('Anio').size().sum())
axA.annotate('2020: pandemia\n(mínimo de la serie)', xy=(2020, 3), xytext=(2013.6, 3.5),
             fontsize=8.5, color='#444444',
             arrowprops=dict(arrowstyle='->', color='#888888', lw=1))
axA.annotate('2001-02: crisis\nargentina', xy=(2002, 9), xytext=(2003.2, 2.5),
             fontsize=8.5, color='#444444',
             arrowprops=dict(arrowstyle='->', color='#888888', lw=1))
axA.set_title('A. El latido de la diplomacia regional: tramos completados por año\n'
              '(ARG+BRA+CHL; el multilateral es el piso estable, el bilateral la variable de ajuste)',
              fontsize=10.5, fontweight='bold', loc='left')
axA.set_ylabel('Tramos completados')
axA.set_xticks(range(2000, 2027, 4))
axA.legend(frameon=False, loc='upper right', fontsize=9)
axA.spines[['top', 'right']].set_visible(False)

# ── B) Geografía invertida ─────────────────────────────────────────────────
axB = fig.add_subplot(gs[0, 1])
df['DestinoAgr'] = np.select(
    [df['Destination_Country'] == 'United States',
     df['Destination_Region'] == 'South America',
     df['Destination_Region'] == 'Europe',
     df['Destination_Region'] == 'Asia-Pacific',
     df['Destination_Region'].isin(['Central America', 'Caribbean']) |
     ((df['Destination_Region'] == 'North America') & (df['Destination_Country'] != 'United States')),
     df['Destination_Region'] == 'Middle East',
     df['Destination_Region'] == 'Africa'],
    ['EEUU', 'Sudamérica', 'Europa', 'Asia-Pacífico', 'Resto de ALC', 'Medio Oriente', 'África'],
    default='Otro')
tab = (df[df['Visit_Category'].isin(['Bilateral', 'Multilateral'])]
       .groupby(['DestinoAgr', 'Visit_Category']).size().unstack(fill_value=0))
tab = tab.loc[tab.sum(axis=1).sort_values().index]
y = np.arange(len(tab))
axB.barh(y + 0.2, tab['Bilateral'], height=0.38, color=C_BI, label='Bilateral')
axB.barh(y - 0.2, tab['Multilateral'], height=0.38, color=C_MU, label='Multilateral')
for yi, (b, m) in zip(y, zip(tab['Bilateral'], tab['Multilateral'])):
    axB.text(b + 1.5, yi + 0.2, str(int(b)), va='center', fontsize=8, color=C_BI)
    axB.text(m + 1.5, yi - 0.2, str(int(m)), va='center', fontsize=8, color=C_MU)
axB.set_yticks(y)
axB.set_yticklabels(tab.index, fontsize=9.5)
axB.set_title('B. La geografía invertida (total 2000–2026):\n'
              'a EEUU se va por cumbres, a Europa por visitas de Estado',
              fontsize=10.5, fontweight='bold', loc='left')
axB.set_xlabel('Tramos completados')
axB.legend(frameon=False, loc='lower right', fontsize=9)
axB.spines[['top', 'right']].set_visible(False)

# ── C) Olas regionales (heatmap) ───────────────────────────────────────────
axC = fig.add_subplot(gs[1, 0])
orden_reg = ['South America', 'Europe', 'North America', 'Asia-Pacific',
             'Central America', 'Caribbean', 'Middle East', 'Africa']
et_reg = ['Sudamérica', 'Europa', 'Norteamérica', 'Asia-Pacífico',
          'Centroamérica', 'Caribe', 'Medio Oriente', 'África']
mat = np.zeros((len(orden_reg), len(ANIOS)))
piv = df.groupby(['Destination_Region', 'Anio']).size()
for i, reg in enumerate(orden_reg):
    for j, a in enumerate(ANIOS):
        mat[i, j] = piv.get((reg, a), 0)
im = axC.imshow(mat, aspect='auto', cmap='YlOrRd', interpolation='nearest')
axC.set_yticks(range(len(et_reg)))
axC.set_yticklabels(et_reg, fontsize=9)
axC.set_xticks(range(0, len(ANIOS), 4))
axC.set_xticklabels(ANIOS[::4])
axC.set_title('C. Olas regionales: destino de los tramos por año\n'
              '(la ola africana de Lula 2003-2010; el ascenso asiático; el vacío de 2020)',
              fontsize=10.5, fontweight='bold', loc='left')
plt.colorbar(im, ax=axC, shrink=0.8, label='Tramos')

# ── D) Perfiles presidenciales ─────────────────────────────────────────────
axD = fig.add_subplot(gs[1, 1])
MANDATOS = {  # prefijo: (etiqueta, pais, anios de mandato dentro de la ventana 2000-2026)
    'ARG-DLR': ('De la Rúa', 'Argentina', 1.97), 'ARG-EDU': ('Duhalde', 'Argentina', 1.39),
    'ARG-NK': ('N. Kirchner', 'Argentina', 4.55), 'ARG-CFK': ('CFK', 'Argentina', 8.0),
    'ARG-MM': ('Macri', 'Argentina', 4.0), 'ARG-AF': ('A. Fernández', 'Argentina', 4.0),
    'ARG-JM': ('Milei', 'Argentina', 2.58),
    'BRA-FHC': ('Cardoso', 'Brasil', 3.0), 'BRA-LU': ('Lula I-II', 'Brasil', 8.0),
    'BRA-DR': ('Dilma', 'Brasil', 5.36), 'BRA-MT': ('Temer', 'Brasil', 2.64),
    'BRA-JB': ('Bolsonaro', 'Brasil', 4.0), 'BRA-LU3': ('Lula III', 'Brasil', 3.52),
    'CHL-RL': ('Lagos', 'Chile', 6.0), 'CHL-MB1': ('Bachelet I', 'Chile', 4.0),
    'CHL-SP1': ('Piñera I', 'Chile', 4.0), 'CHL-MB2': ('Bachelet II', 'Chile', 4.0),
    'CHL-SP2': ('Piñera II', 'Chile', 4.0), 'CHL-GB': ('Boric', 'Chile', 4.0),
    # CHL-JAK (Kast) excluido: 0.32 anios de mandato, muestra insuficiente
}
for pref, (et, pais, anios) in MANDATOS.items():
    d = df[df['Prefijo'] == pref]
    viajes = d['Journey_ID'].nunique()
    bi_mu = d[d['Visit_Category'].isin(['Bilateral', 'Multilateral'])]
    pm = 100 * (bi_mu['Visit_Category'] == 'Multilateral').mean()
    x = viajes / anios
    axD.scatter(x, pm, s=viajes * 6, color=C_PAIS[pais], alpha=0.75,
                edgecolor='white', linewidth=0.8, zorder=3)
    axD.annotate(et, (x, pm), textcoords='offset points', xytext=(5, 4), fontsize=7.8)
axD.axhline(50, color='#999999', lw=0.8, ls=':')
axD.text(0.3, 51.5, '50% (paridad bilateral/multilateral)', fontsize=7.5, color='#777777')
axD.set_title('D. Perfiles presidenciales: intensidad viajera vs vocación multilateral\n'
              '(tamaño = viajes físicos totales; Kast excluido por muestra corta)',
              fontsize=10.5, fontweight='bold', loc='left')
axD.set_xlabel('Viajes físicos completados por año de mandato')
axD.set_ylabel('% de tramos multilaterales')
axD.set_ylim(0, 100)
axD.yaxis.set_major_formatter(mticker.PercentFormatter())
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=c, ms=8, label=p)
           for p, c in C_PAIS.items()]
axD.legend(handles=handles, frameon=False, loc='lower right', fontsize=9)
axD.spines[['top', 'right']].set_visible(False)

fig.suptitle('26 años de diplomacia presidencial sudamericana (ARG · BRA · CHL, 2000–2026)\n'
             'El multilateralismo como piso, la geografía invertida por destino y los perfiles de cada presidencia',
             fontsize=14, fontweight='bold')
fig.text(0.01, 0.005,
         'Fuente: Proyecto Viajes Presidenciales, base v1.4 (corte 2026-07-07). Solo tramos/viajes completados. '
         'Brechas conocidas: Milei ene-mar 2026 y Lula dic 2025-mar 2026 (ver PENDIENTES); posible subcaptura de bilaterales cortas en Chile.',
         fontsize=7.5, color='#555555')
fig.subplots_adjust(left=0.07, right=0.97, top=0.885, bottom=0.075)
plt.savefig('fig7_sintesis_analitica.png', dpi=150, bbox_inches='tight')
plt.close()
print('OK fig7')
