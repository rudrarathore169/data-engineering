import streamlit as st
st.title("read and display data frame")

import pandas as pd
df=pd.read_csv('IRIS.csv')

if(st.button("display dataframe")):
    st.write("display dataframe")
    st.dataframe(df)

