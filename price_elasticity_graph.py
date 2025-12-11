import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import the data
df = pd.read_csv('data/Housing_Rent_Price_Volume.csv')

# Clean the data
df['Average Price (£)'] = df['Average Price (£)'].str.replace(',', '').astype(float)
df['Counts of Rents'] = df['Counts of Rents'].str.replace(',', '').astype(float)

# ===== Plot 1: Rent vs Sales Volume =====
# Create first figure
fig1, ax1 = plt.subplots(figsize=(12, 8))
# Interpret: High rent + low sales = strong rental market
#           Low rent + high sales = affordable market

scatter1 = ax1.scatter(df['Average Monthly Rent (£)'], 
                       df['Average Sales Volume '],
                       s=150, 
                       c=df['Gross Yield (%)'],
                       cmap='RdYlGn',
                       alpha=0.7,
                       edgecolors='black',
                       linewidth=1)

# Add quadrant lines to show market types
median_rent = df['Average Monthly Rent (£)'].median()
median_sales = df['Average Sales Volume '].median()

ax1.axvline(median_rent, color='gray', linestyle='--', alpha=0.5, linewidth=1)
ax1.axhline(median_sales, color='gray', linestyle='--', alpha=0.5, linewidth=1)

# Add quadrant labels
ax1.text(df['Average Monthly Rent (£)'].min() * 1.0, 
         df['Average Sales Volume '].max() * 0.995,
         'Affordable Market\n(Low Rent, High Sales)', 
         fontsize=10, style='italic', alpha=0.6, ha='left', va='top',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))

ax1.text(df['Average Monthly Rent (£)'].max() * 0.85, 
         df['Average Sales Volume '].max() * 0.95,
         'High Rent\nHigh Sales', 
         fontsize=10, style='italic', alpha=0.6, ha='center')

ax1.text(df['Average Monthly Rent (£)'].max() * 0.85, 
         df['Average Sales Volume '].min() * 1.5,
         'Strong Rental Market\n(High Rent, Low Sales)', 
         fontsize=10, style='italic', alpha=0.6, ha='center',
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.3))

ax1.text(df['Average Monthly Rent (£)'].min() * 1.2, 
         df['Average Sales Volume '].min() * 1.5,
         'Low Rent\nLow Sales', 
         fontsize=10, style='italic', alpha=0.6, ha='center')

# Annotate key boroughs
for idx, row in df.iterrows():
    if row['Average Monthly Rent (£)'] > 2500 or row['Average Sales Volume '] > 350:
        # Smart positioning based on location
        if row['Average Monthly Rent (£)'] > 2800:  # Far right, move label left
            xytext = (-80, -15)
        elif row['Average Sales Volume '] > 350:  # Top, move label down and left
            xytext = (-60, -20)
        else:
            xytext = (10, 10)
        
        ax1.annotate(row['Boroughs'], 
                    (row['Average Monthly Rent (£)'], row['Average Sales Volume ']),
                    fontsize=8, alpha=0.8, xytext=xytext, 
                    textcoords='offset points',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.7),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0', color='gray', lw=0.5))

ax1.set_xlabel('Average Monthly Rent (£)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Average Sales Volume', fontsize=12, fontweight='bold')
ax1.set_title('Rental Market Strength Analysis\nRent vs Sales Volume', 
              fontsize=13, fontweight='bold', pad=15)
ax1.grid(True, alpha=0.3)

cbar1 = plt.colorbar(scatter1, ax=ax1)
cbar1.set_label('Gross Yield (%)', fontsize=10, fontweight='bold')

fig1.suptitle('2018 Price Elasticity - Rental Market Strength Analysis', 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# ===== Plot 2: Renters (Count of Rents) vs Average Price =====
# Create second figure
fig2, ax2 = plt.subplots(figsize=(12, 8))
# Interpret: Shows which boroughs are "renter-heavy" due to affordability issues

scatter2 = ax2.scatter(df['Average Price (£)'], 
                       df['Counts of Rents'],
                       s=150, 
                       c=df['Average Monthly Rent (£)'],
                       cmap='YlOrRd',
                       alpha=0.7,
                       edgecolors='black',
                       linewidth=1)

# Add trend line
z = np.polyfit(df['Average Price (£)'], df['Counts of Rents'], 1)
p = np.poly1d(z)
ax2.plot(df['Average Price (£)'], p(df['Average Price (£)']), 
         "r--", alpha=0.5, linewidth=2, label='Trend Line')

# Add quadrant lines
median_price = df['Average Price (£)'].median()
median_renters = df['Counts of Rents'].median()

ax2.axvline(median_price, color='gray', linestyle='--', alpha=0.5, linewidth=1)
ax2.axhline(median_renters, color='gray', linestyle='--', alpha=0.5, linewidth=1)

# Add quadrant labels
ax2.text(df['Average Price (£)'].min() * 1.02, 
         df['Counts of Rents'].max() * 0.98,
         'Affordable &\nRenter-Heavy', 
         fontsize=10, style='italic', alpha=0.6, ha='left', va='top',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))

ax2.text(df['Average Price (£)'].max() * 0.85, 
         df['Counts of Rents'].max() * 0.95,
         'Expensive &\nRenter-Heavy', 
         fontsize=10, style='italic', alpha=0.6, ha='center',
         bbox=dict(boxstyle='round', facecolor='orange', alpha=0.3))

ax2.text(df['Average Price (£)'].max() * 0.85, 
         df['Counts of Rents'].min() * 2,
         'Expensive &\nOwner-Heavy', 
         fontsize=10, style='italic', alpha=0.6, ha='center')

ax2.text(df['Average Price (£)'].min() * 1.2, 
         df['Counts of Rents'].min() * 2,
         'Affordable &\nOwner-Heavy', 
         fontsize=10, style='italic', alpha=0.6, ha='center')

# Annotate key boroughs
for idx, row in df.iterrows():
    if row['Counts of Rents'] > 3500 or row['Average Price (£)'] > 1200000:
        # Smart positioning based on location
        if row['Average Price (£)'] > 1200000:  # Far right (Kensington), move label left and down
            xytext = (-80, -25)
        elif row['Counts of Rents'] > 3500:  # Top, move label down
            xytext = (10, -20)
        else:
            xytext = (10, 10)
        
        ax2.annotate(row['Boroughs'], 
                    (row['Average Price (£)'], row['Counts of Rents']),
                    fontsize=8, alpha=0.8, xytext=xytext, 
                    textcoords='offset points',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.7),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0', color='gray', lw=0.5))

ax2.set_xlabel('Average House Price (£)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Count of Renters', fontsize=12, fontweight='bold')
ax2.set_title('Affordability vs Rental Demand\nRenters vs Average Price', 
              fontsize=13, fontweight='bold', pad=15)
ax2.grid(True, alpha=0.3)
ax2.legend(loc='upper left', fontsize=9)

cbar2 = plt.colorbar(scatter2, ax=ax2)
cbar2.set_label('Avg Monthly Rent (£)', fontsize=10, fontweight='bold')

fig2.suptitle('2018 Price Elasticity - Affordability vs Rental Demand', 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# ===== Plot 3: Sales Volume vs House Price =====
# Create third figure
fig3, ax3 = plt.subplots(figsize=(12, 8))
# Interpret: Shows relationship between market activity and property values

scatter3 = ax3.scatter(df['Average Price (£)'], 
                       df['Average Sales Volume '],
                       s=150, 
                       c=df['Gross Yield (%)'],
                       cmap='RdYlGn',
                       alpha=0.7,
                       edgecolors='black',
                       linewidth=1)

# Add trend line
z3 = np.polyfit(df['Average Price (£)'], df['Average Sales Volume '], 1)
p3 = np.poly1d(z3)
ax3.plot(df['Average Price (£)'], p3(df['Average Price (£)']), 
         "b--", alpha=0.5, linewidth=2, label='Trend Line')

# Add quadrant lines
median_price_3 = df['Average Price (£)'].median()
median_sales_3 = df['Average Sales Volume '].median()

ax3.axvline(median_price_3, color='gray', linestyle='--', alpha=0.5, linewidth=1)
ax3.axhline(median_sales_3, color='gray', linestyle='--', alpha=0.5, linewidth=1)

# Add quadrant labels
ax3.text(df['Average Price (£)'].min() * 1.0, 
         df['Average Sales Volume '].max() * 0.995,
         'Affordable &\nHigh Activity', 
         fontsize=10, style='italic', alpha=0.6, ha='left', va='top',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))

ax3.text(df['Average Price (£)'].max() * 0.85, 
         df['Average Sales Volume '].max() * 0.95,
         'Expensive &\nHigh Activity', 
         fontsize=10, style='italic', alpha=0.6, ha='center',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.3))

ax3.text(df['Average Price (£)'].max() * 0.85, 
         df['Average Sales Volume '].min() * 1.5,
         'Expensive &\nLow Activity', 
         fontsize=10, style='italic', alpha=0.6, ha='center',
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.3))

ax3.text(df['Average Price (£)'].min() * 1.2, 
         df['Average Sales Volume '].min() * 1.5,
         'Affordable &\nLow Activity', 
         fontsize=10, style='italic', alpha=0.6, ha='center')

# Annotate key boroughs
for idx, row in df.iterrows():
    if row['Average Sales Volume '] > 350 or row['Average Price (£)'] > 1200000:
        # Smart positioning based on location
        if row['Average Price (£)'] > 1200000:  # Far right (Kensington), move label left
            xytext = (-80, -25)
        elif row['Average Sales Volume '] > 350:  # High sales, move label down
            xytext = (10, -20)
        else:
            xytext = (10, 10)
        
        ax3.annotate(row['Boroughs'], 
                    (row['Average Price (£)'], row['Average Sales Volume ']),
                    fontsize=8, alpha=0.8, xytext=xytext, 
                    textcoords='offset points',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.7),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0', color='gray', lw=0.5))

ax3.set_xlabel('Average House Price (£)', fontsize=12, fontweight='bold')
ax3.set_ylabel('Average Sales Volume', fontsize=12, fontweight='bold')
ax3.set_title('Market Activity vs Property Values\nSales Volume vs House Price', 
              fontsize=13, fontweight='bold', pad=15)
ax3.grid(True, alpha=0.3)
ax3.legend(loc='upper left', fontsize=9)

cbar3 = plt.colorbar(scatter3, ax=ax3)
cbar3.set_label('Gross Yield (%)', fontsize=10, fontweight='bold')

fig3.suptitle('2018 Price Elasticity - Market Activity Analysis', 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
