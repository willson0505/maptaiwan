import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.title("中央研究院 1934 年日治臺灣全圖（1:300,000 第三版）")

# 初始化地圖（中心點設在台灣）
m = folium.Map(location=[23.5, 121], zoom_start=7)

# 加入中央研究院 1934 地圖作為底圖
folium.TileLayer(
    tiles="https://gis.sinica.edu.tw/tileserver/tiles/JM300K_1934/{z}/{x}/{y}.png",
    attr="中央研究院GIS中心",
    name="日治時期 1934 地圖",
    overlay=False,
    control=True
).add_to(m)

# 加入圖層控制器（如果你之後還想加入其他圖層）
folium.LayerControl().add_to(m)

# 在 Streamlit 中顯示 folium 地圖
st_data = st_folium(m, width=1000, height=700)

