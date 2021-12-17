import streamlit as st 

options = st.multiselect('Choisissez une ou plusieurs région(s)?',("US","Europe","Japan"))

st.write('Vous avez sélectionné:', str(options))
