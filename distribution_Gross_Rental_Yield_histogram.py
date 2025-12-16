import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# Load data
df = pd.read_csv('data/Housing_Rent_Price_Volume.csv')

# Extract yield series
yield_series = df['Gross Yield (%)'].astype(float)
median_yield = yield_series.median()

# Style
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Histogram
bins = 12
ax.hist(yield_series, bins=bins, color='#4C72B0', alpha=0.65, edgecolor='white', label='Histogram')

# KDE
x_vals = np.linspace(yield_series.min() * 0.95, yield_series.max() * 1.05, 200)
kde = gaussian_kde(yield_series)
kde_vals = kde(x_vals)
ax.plot(x_vals, kde_vals * len(yield_series) * (yield_series.max() - yield_series.min()) / bins, 
        color='#C44E52', linewidth=2.2, label='KDE')

# Median line
ax.axvline(median_yield, color='black', linestyle='--', linewidth=1.8, label=f'Median = {median_yield:.2f}%')

# Labels and title
ax.set_xlabel('Gross Rental Yield (%)', fontsize=12, fontweight='bold')
ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax.set_title('Distribution of Gross Rental Yield Across London Boroughs', fontsize=14, fontweight='bold')

ax.legend(frameon=False)
plt.tight_layout()

# Save figure
plt.savefig('Appendix_Figure_A1_Gross_Yield_Distribution.png', dpi=300)
plt.show()
