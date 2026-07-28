# -*- coding: utf-8 -*-
"""
graficos_multilaterales_totales.py — QC visual (2026-07-07).
Evolucion ANUAL PUNTUAL (sin suavizado) de tramos MULTILATERALES COMPLETADOS hacia
(a) EEUU, (b) Sudamerica y (c) Europa, TOTAL AGREGADO de los tres paises de origen
(Argentina + Brasil + Chile), 2000-2026. Fuente: base_consolidada.csv (v1.4).
"""
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

plt.style.use('seaborn-v0_8-whitegrid')

rows = list(csv.DictReader(open('04_BASE_FINAL/base_consolidada.csv', encoding='utf-8')))
df = pd.DataFrame(rows)
df = df[(df['Trip_Status'] == 'Completed') & (df['Visit_Category'] == 'Multilateral')].copy()
df['Anio'] = df['Start_Date'].str[:4].astype(int)

ANIOS = range(2000, 2027)
destinos = {
    'Multilaterales en Estados Unidos': (df['Destination_Country'] == 'United States', '#0173B2'),
    'Multilaterales en países de Sudamérica': (df['Destination_Region'] == 'South America', '#029E73'),
    'Multilaterales en Europa': (df['Destination_Region'] == 'Europe', '#D55E00'),
}

fig, axes = plt.subplots(3, 1, figsize=(11, 11), sharex=True, sharey=True)
for ax, (titulo, (mask, color)) in zip(axes, destinos.items()):
    s = df[mask].groupby('Anio').size().reindex(ANIOS, fill_value=0)
    ax.plot(s.index, s.values, marker='o', ms=5, lw=1.9, color=color)
    ax.set_title(f'{titulo}  (total del período: {int(s.sum())})', fontsize=12, fontweight='bold', loc='left')
    ax.set_ylabel('Tramos multilaterales')
    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ax.spines[['top', 'right']].set_visible(False)
axes[-1].set_xlabel('Año')
axes[-1].set_xticks(range(2000, 2027, 2))
fig.suptitle('Diplomacia multilateral agregada de Argentina + Brasil + Chile (2000–2026):\n'
             'total anual de tramos multilaterales completados por destino',
             fontsize=13.5, fontweight='bold')
fig.text(0.01, 0.005,
         'Unidad: tramos país-visita multilaterales completados (cumbres, foros, asunciones), suma de los tres países de origen; dato anual puntual, sin suavizado.\n'
         'Escala compartida. Brechas conocidas: Milei ene-mar 2026 y Lula dic 2025-mar 2026 sin cobertura verificada (ver PENDIENTES).',
         fontsize=7.5, color='#555555')
plt.tight_layout(rect=[0, 0.025, 1, 0.95])
plt.savefig('fig6_multilaterales_totales_por_destino.png', dpi=150, bbox_inches='tight')
plt.close()
print('OK fig6')
