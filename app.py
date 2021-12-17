import streamlit as st 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache
def get_data ():
  link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
  df = pd.read_csv(link)
  df["continent"]=df["continent"].apply(lambda x : x.strip(".") )
  df.set_index("continent", inplace=True)
  return df

try :
  df = get_data()
  countries = st.multiselect("Choose countries", list(df.index), ["US.","Japan.","Europe."])
  
  if not countries : 
    
    st.error("Please select at least one country.")
  
  else :
    
    data = df.loc[countries]
    viz_correlation = sns.heatmap(data.corr(),center=0,cmap= sns.color_palette("vlog", as_cmap=True))
    st.pyplot(viz_correlation.figure)
