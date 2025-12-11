import pandas as pd
import matplotlib.pyplot as plt

# Import the data
df = pd.read_csv('data/Housing_Rent_Price_Volume.csv')

# Clean the Average Price column (remove commas and convert to numeric)
df['Average Price (£)'] = df['Average Price (£)'].str.replace(',', '').astype(float)

# Create scatter plot
plt.figure(figsize=(12, 8))
plt.scatter(df['Average Monthly Rent (£)'], df['Average Price (£)'], 
            s=100, alpha=0.6, c='steelblue', edgecolors='black', linewidth=0.5)

# Add labels for each point with borough names
for i, borough in enumerate(df['Boroughs']):
    plt.annotate(borough, 
                (df['Average Monthly Rent (£)'].iloc[i], df['Average Price (£)'].iloc[i]),
                fontsize=8, alpha=0.7, ha='right')

plt.xlabel('Average Monthly Rent (£)', fontsize=12)
plt.ylabel('Average Price (Millions £)', fontsize=12)
plt.title('Relationship between Average Monthly Rent and Average House Price\nLondon Boroughs', 
          fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
