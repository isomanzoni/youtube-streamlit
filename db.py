import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import pyodbc
st.title('seramlit DB')
########connect DB 
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\path\to\mydb.accdb;'
    )
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\A\Documents\BaoZ\DB\BaoZ.ex.mdb;'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()

#for table_info in crsr.tables(tableType='TABLE'):
#    print(table_info.table_name)

sql_create_table = ("select 馬番,馬名 from 出走馬T where 競走コード = 22201080601 order by 馬番;")
crsr.execute(sql_create_table)
for row in crsr.fetchall():
   print(row[1])

df1 = pd.DataFrame(pd.read_sql(sql_create_table,cnxn))
st.write(df1,width=400,height=800)

# st.write('DataFrame')
# st.write('Display Image')
######image
# img = Image.open('asuka.jpg')
# st.image(img,caption="飛鳥",use_column_width=True)
# df = pd.DataFrame({ 
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40]
#     })

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