import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title('seramlit 超入門')

# st.write('DataFrame')
st.write('Display Image')
######image
img = Image.open('asuka.jpg')
st.image(img,caption="飛鳥",use_column_width=True)
df = pd.DataFrame({ 
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
    })

#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0),width=200,height=200)
#st.table(df.style.highlight_max(axis=0))
#st.markdown('Streamlit is **_really_ cool**.')

# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )
# #st.line_chart(df)
# df =pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )
# st.map(df)