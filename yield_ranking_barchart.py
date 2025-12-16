import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/Housing_Rent_Price_Volume.csv')

# Prepare data
plot_df = df[['Boroughs', 'Gross Yield (%)']].copy()
plot_df['Gross Yield (%)'] = plot_df['Gross Yield (%)'].astype(float)
plot_df = plot_df.sort_values('Gross Yield (%)', ascending=False)

# Style
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 12))

# Bar chart
bars = ax.barh(plot_df['Boroughs'], plot_df['Gross Yield (%)'], color='#4C72B0', alpha=0.8)
ax.invert_yaxis()  # Highest at top

# Annotate values
for bar, val in zip(bars, plot_df['Gross Yield (%)']):
    ax.text(val + 0.05, bar.get_y() + bar.get_height()/2, f'{val:.2f}%',
            va='center', ha='left', fontsize=9)

# Labels and title
ax.set_xlabel('Gross Rental Yield (%)', fontsize=12, fontweight='bold')
ax.set_ylabel('London Borough', fontsize=12, fontweight='bold')
ax.set_title('Gross Rental Yield Ranking Across London Boroughs', fontsize=14, fontweight='bold', pad=12)

# Clean look
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(axis='x', alpha=0.2, linestyle='--')
plt.tight_layout()

# Save figure
plt.savefig('Appendix_Figure_Yield_Ranking.png', dpi=300)
plt.show()
