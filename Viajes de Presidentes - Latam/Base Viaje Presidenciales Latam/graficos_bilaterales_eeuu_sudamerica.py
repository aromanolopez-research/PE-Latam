# -*- coding: utf-8 -*-
"""
graficos_bilaterales_eeuu_sudamerica.py — QC visual (2026-07-07, v2).
Evolucion ANUAL PUNTUAL (sin suavizado) de tramos BILATERALES COMPLETADOS hacia
(a) EEUU, (b) Sudamerica y (c) Europa, por pais de origen (ARG, BRA, CHL), 2000-2026.
Fuente: base_consolidada.csv (v1.4).
"""
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

plt.style.use('seaborn-v0_8-whitegrid')

rows = list(csv.DictReader(open('04_BASE_FINAL/base_consolidada.csv', encoding='utf-8')))
df = pd.DataFrame(rows)
df = df[(df['Trip_Status'] == 'Completed') & (df['Visit_Category'] == 'Bilateral')].copy()
df['Anio'] = df['Start_Date'].str[:4].astype(int)

PAISES = ['Argentina', 'Brasil', 'Chile']
COLORES = {'Argentina': '#56B4E9', 'Brasil': '#009E73', 'Chile': '#D55E00'}
ANIOS = range(2000, 2027)

destinos = {
    'Bilaterales a Estados Unidos': df['Destination_Country'] == 'United States',
    'Bilaterales a países de Sudamérica': df['Destination_Region'] == 'South America',
    'Bilaterales a Europa': df['Destination_Region'] == 'Europe',
}

fig, axes = plt.subplots(3, 1, figsize=(11, 12), sharex=True, sharey=True)
for ax, (titulo, mask) in zip(axes, destinos.items()):
    d = df[mask]
    for pais in PAISES:
        s = (d[d['Origin_Country'] == pais].groupby('Anio').size()
             .reindex(ANIOS, fill_value=0))
        ax.plot(s.index, s.values, marker='o', ms=4.5, lw=1.6, color=COLORES[pais], label=pais)
    ax.set_title(titulo, fontsize=12, fontweight='bold', loc='left')
    ax.set_ylabel('Tramos bilaterales')
    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ax.spines[['top', 'right']].set_visible(False)
axes[0].legend(frameon=False, loc='upper right')
axes[-1].set_xlabel('Año')
axes[-1].set_xticks(range(2000, 2027, 2))
fig.suptitle('Destinos de la diplomacia bilateral de Argentina, Brasil y Chile (2000–2026):\n'
             'Sudamérica y Europa se disputan el primer lugar (Europa lidera en Brasil); EEUU corre de atrás',
             fontsize=13, fontweight='bold')
fig.text(0.01, 0.005,
         'Unidad: tramos país-visita bilaterales completados; dato anual puntual, sin suavizado. Escala compartida entre paneles.\n'
         'Brechas conocidas: Milei ene-mar 2026 y Lula dic 2025-mar 2026 sin cobertura verificada; posible subcaptura de bilaterales cortas en Chile (ver PENDIENTES).',
         fontsize=7.5, color='#555555')
plt.tight_layout(rect=[0, 0.025, 1, 0.955])
plt.savefig('fig4_bilaterales_eeuu_sudamerica_europa.png', dpi=150, bbox_inches='tight')
plt.close()
print('OK fig4 v2')
