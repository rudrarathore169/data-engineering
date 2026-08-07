import streamlit as st
import pandas as pd

st.title("file uploader")

uploaded_file=st.file_uploader("choose csv file",type=["csv"])

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write("your df is here and it has below rows and columns",df.shape)
    st.dataframe(df)
    head1 = df.head()
    descr = df.describe()
    st.write("head",head1)
    st.write("info",infor)
    st.write("describe",descr)
