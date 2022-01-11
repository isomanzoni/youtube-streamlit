import streamlit as st
import time
st.title('stremlit ')
st.write('progress bar')
'Start'
latest_iteration=st.empty()
bar  = st.progress(0)
for i in range(100):
    latest_iteration.text(f'iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'done!!'
left_column,right_column = st.columns(2)
button = left_column.button('display a charactor at the right column')
if button:
    right_column.write('This is the right column.')


expander1 =st.expander('inqire1')
expander1.write('answer1')
expander2 =st.expander('inqire2')
expander2.write('answer2')
expander3 =st.expander('inqire3')
expander3.write('answer3')
# text = st.text_input('let me know our hoppies.')
# condition = st.slider('Whate is your state now?',0,100,50)
# 'your hobies are' ,text
# 'your state now is ',condition
# option = st.selectbox(
#     'let me know your a favorite number!',
#     list(range(1,11))
# )
# 'your favorite number is ',option