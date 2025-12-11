import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Import the data
df = pd.read_csv('data/Housing_Rent_Price_Volume.csv')

# Clean the Average Price column (remove commas and convert to numeric)
df['Average Price (£)'] = df['Average Price (£)'].str.replace(',', '').astype(float)

# Statistical and Regression Analysis
x = df['Average Monthly Rent (£)']
y = df['Average Price (£)']

# Calculate correlation coefficient and p-value
correlation, p_value = stats.pearsonr(x, y)

# Linear regression
slope, intercept, r_value, p_value_reg, std_err = stats.linregress(x, y)
r_squared = r_value**2

# Calculate confidence interval for the regression line
predict_y = slope * x + intercept
residuals = y - predict_y
n = len(x)
dof = n - 2  # degrees of freedom
t_val = stats.t.ppf(0.975, dof)  # 95% confidence interval
std_resid = np.sqrt(np.sum(residuals**2) / dof)

# Create scatter plot
fig, ax = plt.subplots(figsize=(14, 9))
ax.scatter(x, y, s=100, alpha=0.6, c='steelblue', edgecolors='black', linewidth=0.5, label='Data Points')

# Add trend line
x_line = np.linspace(x.min(), x.max(), 100)
y_line = slope * x_line + intercept
ax.plot(x_line, y_line, 'r--', alpha=0.7, linewidth=2, label='Regression Line')

# Add confidence interval
confidence_interval = t_val * std_resid * np.sqrt(1/n + (x_line - x.mean())**2 / np.sum((x - x.mean())**2))
ax.fill_between(x_line, y_line - confidence_interval, y_line + confidence_interval, 
                 alpha=0.2, color='red', label='95% Confidence Interval')

# Add labels for each point with borough names
for i, borough in enumerate(df['Boroughs']):
    ax.annotate(borough, 
                (df['Average Monthly Rent (£)'].iloc[i], df['Average Price (£)'].iloc[i]),
                fontsize=7, alpha=0.6, ha='right')

# Add statistics box
stats_text = f'''Statistical Analysis:
Regression Equation: y = {slope:.2f}x + {intercept:.2f}
R² = {r_squared:.4f}
Correlation (r) = {correlation:.4f}
P-value = {p_value:.2e}
Standard Error = {std_err:.2f}
Significance: {"***" if p_value < 0.001 else "**" if p_value < 0.01 else "*" if p_value < 0.05 else "ns"}'''

props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', bbox=props, family='monospace')

ax.set_xlabel('Average Monthly Rent (£)', fontsize=12, fontweight='bold')
ax.set_ylabel('Average Price (£)', fontsize=12, fontweight='bold')
ax.set_title('Statistical & Regression Analysis:\nAverage Monthly Rent vs Average House Price\nLondon Boroughs', 
          fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.legend(loc='lower right', fontsize=10)
plt.tight_layout()
plt.show()

# Print detailed statistics to console
print("=" * 60)
print("STATISTICAL AND REGRESSION ANALYSIS")
print("=" * 60)
print(f"\nRegression Equation: Price = {slope:.2f} × Rent + {intercept:.2f}")
print(f"\nR-squared (R²): {r_squared:.4f}")
print(f"  → {r_squared*100:.2f}% of variance in house price is explained by rent")
print(f"\nCorrelation Coefficient (r): {correlation:.4f}")
print(f"  → {'Strong' if abs(correlation) > 0.7 else 'Moderate' if abs(correlation) > 0.4 else 'Weak'} positive correlation")
print(f"\nP-value: {p_value:.2e}")
print(f"  → Result is {'highly significant' if p_value < 0.001 else 'significant' if p_value < 0.05 else 'not significant'}")
print(f"\nStandard Error: {std_err:.2f}")
print(f"\nInterpretation:")
print(f"  • For every £1 increase in monthly rent,")
print(f"    house price increases by approximately £{slope:.2f}")
print("=" * 60)
