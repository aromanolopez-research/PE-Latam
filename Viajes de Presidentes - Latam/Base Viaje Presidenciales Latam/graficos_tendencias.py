# -*- coding: utf-8 -*-
"""
graficos_tendencias.py — Control de calidad visual (2026-07-06).
Tendencias Bilateral vs Multilateral para Argentina, Brasil y Chile.

Unidad: TRAMOS (filas país-visita) con Trip_Status = Completed (CODEBOOK sección 7).
Chile: módulo PARCIAL (Lagos a Bachelet 2; faltan Piñera 2 y Boric) y NO integrado.
"""
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

plt.style.use('seaborn-v0_8-whitegrid')

BASE = '04_BASE_FINAL/base_consolidada.csv'
CHL  = '03_MODULOS_PAIS/chile/chile_viajes.csv'

def load(path):
    return pd.DataFrame(list(csv.DictReader(open(path, encoding='utf-8'))))

df = pd.concat([load(BASE), load(CHL)], ignore_index=True)
df = df[df['Trip_Status'] == 'Completed'].copy()
df['Anio'] = df['Start_Date'].str[:4].astype(int)

C_BI, C_MU, C_OT = '#0173B2', '#DE8F05', '#BBBBBB'   # paleta apta daltonismo
PAISES = ['Argentina', 'Brasil', 'Chile']
NOTA_CHL = 'Chile: módulo parcial (Lagos–Bachelet II; faltan Piñera II y Boric), aún no integrado.'

# ── FIG 1: evolución anual por categoría, un panel por país ────────────────
fig, axes = plt.subplots(3, 1, figsize=(11, 10), sharex=True, sharey=True)
anios = range(2000, 2027)
for ax, pais in zip(axes, PAISES):
    d = df[df['Origin_Country'] == pais]
    for cat, color in [('Bilateral', C_BI), ('Multilateral', C_MU)]:
        s = d[d['Visit_Category'] == cat].groupby('Anio').size().reindex(anios, fill_value=0)
        ax.plot(s.index, s.values, marker='o', ms=4, lw=1.8, color=color, label=cat)
    ax.set_title(pais, fontsize=12, fontweight='bold', loc='left')
    ax.spines[['top', 'right']].set_visible(False)
    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ax.set_ylabel('Tramos')
axes[0].legend(frameon=False, loc='upper right')
axes[-1].set_xlabel('Año')
axes[-1].set_xticks(range(2000, 2027, 2))
fig.suptitle('Diplomacia presidencial: tramos completados por año y categoría (2000–2026)',
             fontsize=14, fontweight='bold')
fig.text(0.01, 0.005, NOTA_CHL + ' Unidad: tramos (filas país-visita) completados.',
         fontsize=8, color='#555555')
plt.tight_layout(rect=[0, 0.02, 1, 0.97])
plt.savefig('fig1_evolucion_anual_categoria.png', dpi=150, bbox_inches='tight')
plt.close()

# ── FIG 2: composición % por presidencia (orden cronológico por país) ──────
inicio = df.groupby(['Origin_Country', 'President'])['Start_Date'].min()
comp = (df.groupby(['Origin_Country', 'President', 'Visit_Category']).size()
          .unstack(fill_value=0))
for c in ('Bilateral', 'Multilateral', 'Other'):
    if c not in comp:
        comp[c] = 0
comp['total'] = comp[['Bilateral', 'Multilateral', 'Other']].sum(axis=1)
orden = []
for pais in PAISES:
    pres = inicio.loc[pais].sort_values().index.tolist()
    orden += [(pais, p) for p in pres]
comp = comp.loc[orden]

fig, ax = plt.subplots(figsize=(11, 9))
labels = [f"{p}  ({pa[:3].upper()}, n={int(comp.loc[(pa,p),'total'])})" for pa, p in orden]
y = range(len(orden))[::-1]
bi = (comp['Bilateral'] / comp['total'] * 100).values
mu = (comp['Multilateral'] / comp['total'] * 100).values
ot = (comp['Other'] / comp['total'] * 100).values
ax.barh(y, bi, color=C_BI, label='Bilateral')
ax.barh(y, mu, left=bi, color=C_MU, label='Multilateral')
ax.barh(y, ot, left=bi + mu, color=C_OT, label='Other')
for yi, b in zip(y, bi):
    ax.text(b / 2, yi, f'{b:.0f}%', va='center', ha='center', color='white', fontsize=8)
for yi, b, m in zip(y, bi, mu):
    if m > 5:
        ax.text(b + m / 2, yi, f'{m:.0f}%', va='center', ha='center', color='white', fontsize=8)
ax.set_yticks(list(y))
ax.set_yticklabels(labels, fontsize=9)
ax.set_xlim(0, 100)
ax.xaxis.set_major_formatter(mticker.PercentFormatter())
ax.set_xlabel('Participación sobre el total de tramos completados')
ax.set_title('Perfil diplomático por presidencia: mezcla Bilateral / Multilateral / Other\n'
             '(presidencias en orden cronológico dentro de cada país)',
             fontsize=13, fontweight='bold')
ax.legend(frameon=False, loc='lower right', ncols=3)
ax.spines[['top', 'right']].set_visible(False)
# separadores entre países
cortes = []
acc = 0
for pais in PAISES[:-1]:
    acc += len(inicio.loc[pais])
    cortes.append(len(orden) - acc - 0.5)
for c in cortes:
    ax.axhline(c, color='#888888', lw=0.8, ls='--')
fig.text(0.01, 0.005, NOTA_CHL, fontsize=8, color='#555555')
plt.tight_layout(rect=[0, 0.02, 1, 1])
plt.savefig('fig2_composicion_presidencias.png', dpi=150, bbox_inches='tight')
plt.close()

# ── FIG 3: proporción multilateral anual, tres países comparados ───────────
fig, ax = plt.subplots(figsize=(11, 6))
colores = {'Argentina': '#56B4E9', 'Brasil': '#009E73', 'Chile': '#D55E00'}
for pais in PAISES:
    d = df[(df['Origin_Country'] == pais) & (df['Visit_Category'].isin(['Bilateral', 'Multilateral']))]
    tot = d.groupby('Anio').size()
    mu = d[d['Visit_Category'] == 'Multilateral'].groupby('Anio').size()
    prop = (mu.reindex(tot.index, fill_value=0) / tot * 100)
    suave = prop.rolling(3, center=True, min_periods=1).mean()   # media móvil 3 años
    ax.plot(prop.index, prop.values, 'o', ms=3.5, alpha=0.35, color=colores[pais])
    ax.plot(suave.index, suave.values, lw=2.2, color=colores[pais], label=pais)
ax.axhline(50, color='#999999', lw=0.8, ls=':')
ax.text(2000.2, 51.5, '50% (paridad)', fontsize=8, color='#777777')
ax.set_ylim(0, 100)
ax.yaxis.set_major_formatter(mticker.PercentFormatter())
ax.set_xticks(range(2000, 2027, 2))
ax.set_xlabel('Año')
ax.set_ylabel('% de tramos multilaterales')
ax.set_title('¿Cuánto pesa lo multilateral en la agenda? Proporción anual de tramos multilaterales\n'
             '(puntos: dato anual · líneas: media móvil de 3 años)',
             fontsize=13, fontweight='bold')
ax.legend(frameon=False, loc='upper right')
ax.spines[['top', 'right']].set_visible(False)
fig.text(0.01, 0.005, NOTA_CHL + ' Excluye categoría Other.', fontsize=8, color='#555555')
plt.tight_layout(rect=[0, 0.02, 1, 1])
plt.savefig('fig3_proporcion_multilateral.png', dpi=150, bbox_inches='tight')
plt.close()

# resumen numérico para el control de calidad
print(df.groupby(['Origin_Country', 'Visit_Category']).size().unstack(fill_value=0))
print()
print('Tramos completados por país:', df.groupby('Origin_Country').size().to_dict())
