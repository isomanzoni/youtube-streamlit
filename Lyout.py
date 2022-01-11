import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import pyodbc
st.title('seramlit Lyout')
st.sidebar.write('Side Bar')
text = st.sidebar.text_input('Would you tell us your hobby?')
'your hobby:',text
condition = st.sidebar.slider('What is your condition now?',0,100,50)
'condition:',condition
