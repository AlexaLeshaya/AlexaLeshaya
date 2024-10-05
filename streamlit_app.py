import streamlit as st

st.title('👀 AlexaLeshaya')

st.write('Hello world!')

with st.expander('Initial data'):
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

  st.write('**y**')
  y_raw = df.species
  y_raw
