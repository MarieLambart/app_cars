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

st.set_page_config(layout="wide")

try :
  


  df = get_data()
  countries = st.sidebar.multiselect("Choose countries", list(df.index.unique()))
  
  if not countries : 
    
    st.sidebar.error("Please select at least one country.")
  
  else :
    
    data = df.loc[countries]
    
    c1,c2,c3 = st.columns((1,4,1))
    
    c2.write("### Caracteristics for each cars for country(ies) that you choose.")
    c2.write(data)
    
    c2.write("\n")
    c2.write("\n")
    c2.write("\n")
    
    c1,c2 = st.columns((1,1))


    c1.write("###### Correlation Heatmap of car's dataset for country(ies) that you choose with coefficient.")

    viz_correlation = sns.heatmap(data.corr(),center=0,cmap= sns.diverging_palette(220, 10,  as_cmap=True), vmax=1, vmin=-1,annot=True)

    c1.pyplot(viz_correlation.figure)

    
    c2.write("We can see that there is a strong correlation positive between :")
    c2.write("- Cylinders and Weightlbs, Hp, Cubicinches")
    c2.write("- Cubicinches and Weightlbs, Hp")
    c2.write("- Hp and Weightlbs")
    c2.write("That's to say if one increases, the other also increases.")
    c2.write("")
    c2.write("and a strong correlation negative bewteen :")
    c2.write("- Mpg and Weightlbs, Hp, Cubicinches, Cylinders")
    c2.write("- Hp and Time-to-60")
    c2.write("That's to say if one increases, the other decreases.")

    

except URLError as e:
  
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )
