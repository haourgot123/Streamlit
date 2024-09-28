import streamlit as st
import numpy as np
import pandas as pd

st.title('🤖 Machine Learning App')
st.info('This is my Machine Learning App')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
  st.write('**x**')
  X_raw = df.drop('species', axis = 1)
  X_raw
  st.write('**y**')
  y_raw = df.species
  y_raw
  
