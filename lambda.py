import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap


data = pd.read_csv("houseprice-with-lonlat.csv")
data.columns
data = data.iloc[:,1:]
data.query("TotRms_AbvGrd >= 13")

# Define the center of the map
map_center = [data['Latitude'].mean(), data['Longitude'].mean()]


data = pd.read_csv("houseprice-with-lonlat.csv")

df = df.iloc[:, 1:]

# 집 가격 범위랑 그에 따른 색 list 만들기 
price_ranges = [100000, 200000, 300000, 400000, 500000, 600000, 700000, float('inf')]
colors = ['blue', 'green', 'orange', 'red', 'purple', 'darkred', 'black', 'grey']

# 가격에 따른 색 지정 
def get_color(price):
    for i, range_upper in enumerate(price_ranges):
        if price <= range_upper:
            return colors[i]

map_center = [data['Latitude'].mean(), data['Longitude'].mean()]

my_map = folium.Map(location=map_center, zoom_start=12,tiles = "cartodbpositron")

for price, lat, lon in zip(data['Sale_Price'], data['Latitude'], data['Longitude']):
    color = get_color(price)
    folium.Circle(
        location=[lat, lon],
        radius=20,
        color=color,
        popup=f"Price: ${price}",
        fill=True,
        fill_opacity=0.6,
    ).add_to(my_map)


corrected_map_path = 'house_price_corrected_colored_map.html'
my_map.save(corrected_map_path)
corrected_map_path



# Create the map
m = folium.Map(location=map_center, zoom_start=12)

# Add points to the map
for _, row in data.iterrows():
    folium.Circle(
        location=[row['Latitude'], row['Longitude']],
        radius=50,
        color='blue',
        fill=True,
        fill_opacity=0.6,
        popup=f"Price: ${row['Sale_Price']}"
    ).add_to(m)

# Save the map as an HTML file and display
map_path = '/mnt/data/house_price_map.html'
m.save(map_path)
map_path

# Ensuring the lists of price_ranges and colors are correctly aligned
price_ranges = [100000, 200000, 300000, 400000, 500000, 600000, 700000, float('inf')]
colors = ['blue', 'green', 'orange', 'red', 'purple', 'darkred', 'black', 'grey']

# Adjust the function to map correctly based on price
def get_color(price):
    for i, range_upper in enumerate(price_ranges):
        if price <= range_upper:
            return colors[i]
    return colors[-1]  # Fallback color for unexpected values

# Create the map with correctly colored markers
m_colored = folium.Map(location=map_center, zoom_start=12)

for _, row in data.iterrows():
    price = row['Sale_Price']
    color = get_color(price)
    folium.Circle(
        location=[row['Latitude'], row['Longitude']],
        radius=50,
        color=color,
        fill=True,
        fill_opacity=0.6,
        popup=f"Price: ${price}"
    ).add_to(m_colored)

# Save the map as an HTML file and display
corrected_map_path = '/mnt/data/house_price_corrected_colored_map.html'
m_colored.save(corrected_map_path)
corrected_map_path
import pandas as pd
import folium
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors
import matplotlib
# 데이터 로드
data = pd.read_csv("houseprice-with-lonlat.csv")

# 인덱스 열 제거
data = data.iloc[:, 1:]

# 팔레트 설정
neighborhoods = data['Neighborhood'].unique()
colors = plt.cm.coolwarm(np.linspace(0, 1, len(neighborhoods)))
neighborhood_color_map = {neighborhood: colors[i] for i, neighborhood in enumerate(neighborhoods)}

# 지도 중심 설정
map_center = [data['Latitude'].mean(), data['Longitude'].mean()]

# 지도 생성
my_map = folium.Map(location=map_center, zoom_start=12, tiles="cartodbpositron")

# 각 주택에 대해 원 그리기
for price, lat, lon, neighborhood in zip(data['Sale_Price'], data['Latitude'], data['Longitude'], data['Neighborhood']):
    color = matplotlib.colors.to_hex(neighborhood_color_map[neighborhood])
    folium.Circle(
        location=[lat, lon],
        radius=20,
        color=color,
        popup=f"Price: ${price}, Neighborhood: {neighborhood}",
        fill=True,
        fill_opacity=0.6,
    ).add_to(my_map)

# 지도를 HTML 파일로 저장
my_map.save('house_prices_map.html')

!pip install geopandas

import pandas as pd
import geopandas as gpd
import folium

# GeoJSON 파일 URL
url = 'https://opendata.arcgis.com/datasets/74d64aebfcd34bcdb48de6c7567bfc87_0.geojson'

# GeoJSON 파일 로드
gdf = gpd.read_file(url)

# GeoDataFrame을 JSON 형식으로 변환
geojson_data = gdf.to_json()

# 강조할 동네 이름 설정
highlight_neighborhood = "Old Town"

# 지도 중심 설정
map_center = [42.034722, -93.620833]  # Ames, Iowa의 중심 좌표

# 지도 생성
my_map = folium.Map(location=map_center, zoom_start=12, tiles="cartodbpositron")

# GeoJSON 데이터 추가
folium.GeoJson(
    geojson_data,
    name="Neighborhoods",
    style_function=lambda feature: {
        'fillColor': 'blue' if feature['properties']['name'] == highlight_neighborhood else 'gray',
        'color': 'black',
        'weight': 2,
        'dashArray': '5, 5' if feature['properties']['name'] == highlight_neighborhood else '1, 1',
        'fillOpacity': 0.5,
    },
    highlight_function=lambda feature: {
        'weight': 3,
        'color': 'black',
        'dashArray': '5, 5'
    },
    tooltip=folium.features.GeoJsonTooltip(fields=['name'], aliases=['Neighborhood:'])
).add_to(my_map)

# 지도 저장
my_map.save('ames_neighborhoods.html')




