#!/usr/bin/env python3
"""Generate NK effect-size bar chart for ECTA paper.

Grouped bar chart: eta-squared by metric across K values at gen 200.
Publication quality for Springer LNCS.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Data from analyze_nk_pilot.py output at generation 200
# Columns: K=0, K=4, K=6
metrics = ['Diversity', 'Mean Fitness', 'Best Fitness']
k_values = ['K = 0', 'K = 4', 'K = 6']

# eta-squared values at gen 200 from the analysis
eta_squared = {
    'Diversity':     [0.0490, 0.4445, 0.6859],
    'Mean Fitness':  [0.0001, 0.3366, 0.3493],
    'Best Fitness':  [0.0000, 0.0999, 0.0855],
}

# Significance markers at gen 200
sig_markers = {
    'Diversity':     ['', '***', '***'],
    'Mean Fitness':  ['', '**', '**'],
    'Best Fitness':  ['', '', ''],
}

fig, ax = plt.subplots(figsize=(5.5, 3.5))

x = np.arange(len(metrics))
width = 0.22
offsets = [-width, 0, width]

colors = ['#bdbdbd', '#6baed6', '#2171b5']

for i, (k_label, color) in enumerate(zip(k_values, colors)):
    vals = [eta_squared[m][i] for m in metrics]
    sigs = [sig_markers[m][i] for m in metrics]
    bars = ax.bar(x + offsets[i], vals, width, label=k_label, color=color,
                  edgecolor='black', linewidth=0.5)
    # Add significance markers
    for bar, sig in zip(bars, sigs):
        if sig:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.015,
                    sig, ha='center', va='bottom', fontsize=8)

ax.set_ylabel(r'Effect size ($\eta^2$)', fontsize=10)
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=9)
ax.set_ylim(0, 0.82)
ax.legend(fontsize=9, loc='upper left')
ax.axhline(y=0.06, color='gray', linestyle=':', linewidth=0.7, alpha=0.5)
ax.axhline(y=0.14, color='gray', linestyle='--', linewidth=0.7, alpha=0.5)
ax.text(2.65, 0.065, 'medium', fontsize=7, color='gray', va='bottom')
ax.text(2.65, 0.145, 'large', fontsize=7, color='gray', va='bottom')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('/home/lyra/projects/memory/drafts/figures/fig6_nk_effect_size.pdf',
            bbox_inches='tight', dpi=300)
plt.savefig('/home/lyra/projects/memory/drafts/figures/fig6_nk_effect_size.png',
            bbox_inches='tight', dpi=300)
print("NK effect size figure saved.")
