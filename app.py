import streamlit as st 
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from urllib.error import URLError

@st.cache
def get_data ():
  link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
  df = pd.read_csv(link)
  df["continent"]=df["continent"].apply(lambda x : x.strip(".") )
  df.set_index("continent", inplace=True)
  return df

try :
  
  col1, col2, col3 = st.columns(3)
  
  
  df = get_data()
  countries = col1.multiselect("Choose countries", list(df.index.unique()))
  
  if not countries : 
    
    st.error("Please select at least one country.")
  
  else :
    
    
   
    
    col2.write("#### Correlation Heatmap of car's dataset for country(ies) that you choose.")
    
    data = df.loc[countries]
    viz_correlation = sns.heatmap(data.corr(),center=0,cmap= sns.diverging_palette(220, 10,  as_cmap=True), vmax=1, vmin=-1)
    
    
    col2.pyplot(viz_correlation.figure)
    
    col3.write("#### Distribution for each caracteristics of car's dataset for country(ies) that you choose.")
    
    col3.pyplot(viz_correlation.figure)

    

except URLError as e:
  
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )
