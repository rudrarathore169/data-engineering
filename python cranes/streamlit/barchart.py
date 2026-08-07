import streamlit as st
import pandas as pd

uploaded_file=st.file_uploader("choose csv file",type=["csv"])

cd = pd.read_csv(uploaded_file)

col = cd.columns

x = st.selectbox('select one column',col)
if(st.button("create chart")):
    st.bar_chart(cd[x])
    
