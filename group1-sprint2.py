
import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import folium
# from streamlit_folium import folium_static
# from PIL import Image
# import geopandas as gpd
# import warnings
# warnings.filterwarnings('ignore')

st.sidebar.title("Maximizing Streams Across VIVA Artists")

st.sidebar.write('')
st.sidebar.write('')

st.sidebar.title("The Team")
st.sidebar.write('Gelo')
st.sidebar.write('Tin')
st.sidebar.write('Niño')
st.sidebar.write('Jopet')
st.sidebar.write('Mentor: Dhee Jee')

st.sidebar.write('')

# df = pd.read_csv("data/PH-HRIR-merged.csv")
# df_1 = pd.read_csv("data/experienced_DV.csv")
# province_df = pd.read_csv('data/province_df.csv')
# my_page = st.sidebar.radio('Violence Against Women (VAW) in the Philippines', ['Dataset', 'Prevailence of VAW', 'VAW Interactive Regional Map', 'Clusters', 'Insights', 'Recommendations'])


my_page = st.sidebar.radio('Page Navigation', ['Introduction', 'Audio Feature Selection', 'AN\'s Streams Over Time', 'Weekly Streams and Top Chart Positions of AN vs. Top 2 Competitors', 'Streams Contribution of AN and Viva Artists', 'Recommendation Engine'])

if my_page == 'Introduction':
    st.image("1.png")

elif my_page == 'Audio Feature Selection':
    st.image("2.png")

elif my_page == 'AN\'s Streams Over Time':
    st.image("3.png")
    
elif my_page == 'Weekly Streams and Top Chart Positions of AN vs. Top 2 Competitors':
    st.image("6.png")
    
elif my_page == 'Streams Contribution of AN and Viva Artists':
    st.image("4.png")
    
elif my_page == 'Recommendation Engine':
    st.image("5.png")
     

    
    
