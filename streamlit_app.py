import streamlit as st
import pandas as pd

st.title('👀 AlexaLeshaya')

st.write('Hello world!')

with st.expander('Initial data'):
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

  st.write('**X**')
  X_raw = df.drop('species', axis = 1)
  X_raw
  
  st.write('**y**')
  y_raw = df.species
  y_raw

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x = 'bill_lenght_nm', y = 'body_mass_g', color = 'species')
