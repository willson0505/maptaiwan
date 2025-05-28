import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("日治時期1934臺灣地圖（中央研究院）")

# 建立 Folium 地圖
m = folium.Map(location=[23.5, 121], zoom_start=7)

# 加入中研院日治地圖底圖
folium.TileLayer(
    tiles="https://gis.sinica.edu.tw/tileserver/tiles/JM300K_1934/{z}/{x}/{y}.png",
    attr="中央研究院GIS中心",
    name="1934年日治臺灣地圖",
    overlay=False,
    control=True
).add_to(m)

# 顯示地圖
st_folium(m, width=700, height=500)
