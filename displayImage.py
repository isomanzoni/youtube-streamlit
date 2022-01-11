import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('seramlit interactive')
st.write('display image')
if st.checkbox('show imsge'):
    img=Image.open('asuka.jpg')
    st.image(img,caption='飛鳥',use_column_width=True)