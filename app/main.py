
import streamlit as st
import pandas as pd
import numpy as np
import os

url = 'https://raw.githubusercontent.com/Alejandro-q99/Financial-APP/main/app/Data/bonos.csv'
df = pd.read_csv(url)
df