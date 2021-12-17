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
  df = get_data()
  countries = st.multiselect("Choose countries", list(df.index.unique()))
  
  if not countries : 
    
    st.error("Please select at least one country.")
  
  else :
    
    data = df.loc[countries]
    viz_correlation = sns.heatmap(data.corr(),center=0,cmap= sns.diverging_palette(220, 10,  as_cmap=True), vmax=1, vmin=-1)
    plt.title('Cars dataset correlation heatmap',fontsize=16, pad=25.0)
    
    st.pyplot(viz_correlation.figure)
    
    mask = np.triu(np.ones_like(data.corr, dtype=np.bool))
    viz_correlation1 = sns.heatmap(data.corr(), mask=mask, cmap=sns.diverging_palette(220, 10, as_cmap=True),annot = True, vmax=1, vmin=-1, center=0, square=True, linewidths=.5)
    plt.title('Cars dataset correlation heatmap \nwith coefficient',fontsize=16, pad=25.0)
    
    st.pyplot(viz_correlation1.figure)
    
    

except URLError as e:
  
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )
