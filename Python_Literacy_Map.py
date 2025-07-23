"""
Mapping Literacy Rates by Country
-----------------------------------
Joins simulated literacy rate data with world shapefile using GeoPandas.
Displays a choropleth map.

Skills:
- Geospatial data processing with geopandas
- Joining attribute data (literacy rates) to geometries
- Choropleth mapping

Note:
GeoPandas downloads the world geometry data via built-in datasets.
"""

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load built-in world geometry from GeoPandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Simulated literacy data (you can replace with real CSV)
literacy_data = {
    'country': ['Turkey', 'Germany', 'India', 'Nigeria', 'Brazil', 'United States of America', 'Pakistan'],
    'literacy_rate': [97.1, 99.0, 77.7, 62.0, 93.2, 99.0, 58.0]
}

df_lit = pd.DataFrame(literacy_data)

# Merge with world map
merged = world.merge(df_lit, how="left", left_on="name", right_on="country")

# Plot choropleth
plt.figure(figsize=(12, 8))
merged.plot(
    column='literacy_rate',
    cmap='YlGnBu',
    legend=True,
    missing_kwds={"color": "lightgrey", "label": "No data"},
    edgecolor='black'
)

plt.title("Global Literacy Rates by Country (Simulated)", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()
