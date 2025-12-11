import pandas as pd
import folium
from folium import Choropleth
import requests
import branca.colormap as cm

# Import the data
df = pd.read_csv('data/Housing_Rent_Price_Volume.csv')

# Load London boroughs GeoJSON from online source
geojson_url = 'https://raw.githubusercontent.com/radoi90/housequest-data/master/london_boroughs.geojson'
response = requests.get(geojson_url)
london_geo = response.json()

# Check the property key name in the GeoJSON
if london_geo['features']:
    sample_properties = london_geo['features'][0]['properties']
    print("Available properties:", sample_properties.keys())
    # Determine the correct key for borough name
    if 'name' in sample_properties:
        borough_key = 'feature.properties.name'
    elif 'NAME' in sample_properties:
        borough_key = 'feature.properties.NAME'
    else:
        # Use the first key that looks like a name
        borough_key = f'feature.properties.{list(sample_properties.keys())[0]}'
    print(f"Using borough key: {borough_key}")
else:
    borough_key = 'feature.properties.name'

# Create a map centered on London with similar style to the reference image
london_map = folium.Map(
    location=[51.5074, -0.1278],
    zoom_start=10,
    tiles='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
    attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
)

# Create custom colormap (yellow to red similar to the reference image)
min_yield = df['Gross Yield (%)'].min()
max_yield = df['Gross Yield (%)'].max()

colormap = cm.LinearColormap(
    colors=['#FFFFCC', '#FFEDA0', '#FED976', '#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C', '#BD0026', '#800026'],
    vmin=min_yield,
    vmax=max_yield,
    caption='Gross Yield (%)'
)

# Create choropleth layer
choropleth = Choropleth(
    geo_data=london_geo,
    name='Gross Yield',
    data=df,
    columns=['Boroughs', 'Gross Yield (%)'],
    key_on=borough_key,
    fill_color='YlOrRd',
    fill_opacity=0.8,
    line_opacity=0.5,
    line_color='white',
    line_weight=1,
    legend_name='Gross Yield (%)',
    nan_fill_color='lightgray'
).add_to(london_map)

# Enhanced tooltips with more information
style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.20, 
                                'weight': 0.1}

# Add GeoJSON with tooltips
property_name_key = borough_key.replace('feature.properties.', '')
for feature in london_geo['features']:
    borough_name = feature['properties'].get(property_name_key, '')
    borough_data = df[df['Boroughs'] == borough_name]
    
    if not borough_data.empty:
        gross_yield = borough_data['Gross Yield (%)'].values[0]
        avg_rent = borough_data['Average Monthly Rent (£)'].values[0]
        avg_price = str(borough_data['Average Price (£)'].values[0]).replace(',', '')
        avg_price = float(avg_price)
        
        tooltip_html = f"""
        <div style="font-family: Arial; font-size: 12px;">
            <b style="font-size: 14px;">{borough_name}</b><br>
            <b>Gross Yield:</b> {gross_yield}%<br>
            <b>Avg Monthly Rent:</b> £{avg_rent:,}<br>
            <b>Avg House Price:</b> £{avg_price:,.0f}
        </div>
        """
        
        folium.GeoJson(
            feature,
            style_function=style_function,
            highlight_function=highlight_function,
            tooltip=folium.Tooltip(tooltip_html, sticky=True)
        ).add_to(london_map)

# Add colormap to the map
colormap.add_to(london_map)

# Add title using HTML
title_html = '''
             <div style="position: fixed; 
                         top: 10px; left: 50px; width: 300px; height: 50px; 
                         background-color: white; border:2px solid grey; z-index:9999; 
                         font-size:16px; font-weight: bold; padding: 10px">
             London Boroughs - Gross Yield Heat Map
             </div>
             '''
london_map.get_root().html.add_child(folium.Element(title_html))

# Save and display the map
london_map.save('london_gross_yield_heatmap.html')
print("Heat map saved as 'london_gross_yield_heatmap.html'")
print("Opening in browser...")

# Open the map in browser
import webbrowser
import os
webbrowser.open('file://' + os.path.abspath('london_gross_yield_heatmap.html'))
