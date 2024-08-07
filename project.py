import pandas as pd
import numpy as np
import seaborn as sns    
import matplotlib.pyplot as plt    




df = pd.read_csv("data/houseprice-with-lonlat.csv")

df = df.iloc[:, 1:]

### 점찍기
data = pd.read_csv("data/houseprice-with-lonlat.csv")


price_ranges = [100000, 200000, 300000, 400000, 500000, 600000, 700000, float('inf')]
colors = ['blue', 'green', 'orange', 'red', 'purple', 'darkred', 'black', 'grey']

#팝업에 여러 종류의 정보를 넣을 수 있음.

def get_color(price):
    for i, range_upper in enumerate(price_ranges):
        if price <= range_upper:
            return colors[i]
    return colors[-1] 
map_center = [data['Latitude'].mean(), data['Longitude'].mean()]


my_map = folium.Map(location=map_center, zoom_start=12,tiles = "cartodbpositron")

for price, lat, lon in zip(data['Sale_Price'], data['Latitude'], data['Longitude']):
    color = get_color(price)
    folium.Circle(
        location=[lat, lon],
        radius=15,
        fill=True,
        fill_opacity=0.6,
        popup=f"Price: ${price}"
    ).add_to(my_map)

'''
for i in range(len(data)):
    price = data['Sale_Price'][i]
    lat = data['Latitude'][i]
    lon = data['Longitude'][i]
    color = get_color(price)
    folium.Circle(
        location=[lat, lon],
        radius=50,
        color=color,
        fill=True,
        fill_opacity=0.6,
        popup=f"Price: ${price}"
    ).add_to(my_map)
'''
# Save the map as an HTML file and display
corrected_map_path = 'data/house_price_corrected_colored_map.html'
my_map.save(corrected_map_path)
corrected_map_path



# 데이터를 불러옵니다
data = pd.read_csv("data/houseprice-with-lonlat.csv")

# 지도 생성
map_center = [data['Latitude'].mean(), data['Longitude'].mean()]
my_map = folium.Map(location=map_center, zoom_start=12)

# 가격에 따른 크기 조정 함수
def get_icon_size(price):
    # 가격에 따라 아이콘 크기 결정 (단위: 픽셀)
    return [price / 10000, price / 10000]

# 집 모양의 아이콘을 표시하고, 가격에 따라 크기를 조정
for _, row in data.iterrows():
    price = row['Sale_Price']
    icon_size = get_icon_size(price)
    
    # HTML 아이콘 정의
    icon_html = f'<i class="fa fa-home" style="color:#FF0000;font-size:{icon_size[0]}px;"></i>'
    icon = folium.DivIcon(html=icon_html)
    
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"Price: ${price}",
        icon=icon
    ).add_to(my_map)
'''
for i in range(len(data)):
    price = data['Sale_Price'][i]
    lat = data['Latitude'][i]
    lon = data['Longitude'][i]
    icon_size = get_icon_size(price)
    
    # HTML 아이콘 정의
    icon_html = f'<i class="fa fa-home" style="color:#FF0000;font-size:{icon_size[0]}px;"></i>'
    icon = folium.DivIcon(html=icon_html)
    
    folium.Marker(
        location=[lat, lon],
        popup=f"Price: ${price}",
        icon=icon
    ).add_to(my_map)
'''
# 지도 저장
my_map.save("house_price_home_icons_map.html")
