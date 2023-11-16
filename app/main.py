
import streamlit as st
import pandas as pd
import numpy as np
from Functions import Processors as pr
from Functions import AutomatedGit as ag
from datetime import datetime

#read
url = 'https://raw.githubusercontent.com/Alejandro-q99/Financial-APP/main/app/Data/bonos.csv'
df = pd.read_csv(url)
#clean
cleaned_data = pr.clean_and_convert_data(df)
df_cleaned = cleaned_data.drop("diferencia", axis=1)



# Ejecutar Scraper
# Boton.
ag.git_add_commit_push("Update + {datetime.now}")



#
st.title("BONOS")

# Mostrar Gráfica.
st.dataframe(df_cleaned)


