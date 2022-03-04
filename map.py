import streamlit as st
import pandas as pd
import numpy as np

st.title('Crime')

# preprocess and clean data
path = open('document.txt', 'r').read().strip()
df_data = pd.read_feather(f'{path}/2018_street.feather')
df_data.drop(columns=['Crime ID', 'Reported by', 'Location', 'LSOA name', 'Context'], inplace=True)
df_data.rename(columns={"Longitude": "lon", "Latitude": "lat"}, inplace=True)
df_data = df_data[~df_data['lon'].isna()]

# Selection boxes for months and crime type
month = st.selectbox(
     'Select months',
     df_data['Month'].unique())

crime = st.selectbox(
     'Select crime type',
     df_data['Crime type'].value_counts().index)

df_data = df_data[df_data['Month']==month]
df_data = df_data[df_data['Crime type']==crime]


st.map(df_data)