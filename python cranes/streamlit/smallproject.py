from tkinter.font import names

import streamlit as st
import pandas as pd


uploaded_file=st.file_uploader("choose csv file",type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

topr = df.head()
st.write(topr)
rows = df.shape[0]
col  = df.shape[1]
st.write(f"it have {rows} rows and {col} columns")
missing_value = df.isnull().sum()
st.write(f"it have {missing_value} missing values")
        #calculating no. of columns have numeric data
columns = df.columns
numerical_cols = df.select_dtypes(include=['number']).columns
categorical_cols = df.select_dtypes(include=['object', 'category']).columns
st.write(f"{numerical_cols} are numerical columns and {categorical_cols} are categorical columns")
selected_xaxis = st.selectbox("choose the x axis column", numerical_cols)
selected_yaxis = st.selectbox("choose the y axis column", numerical_cols)

if st.button("display graphs"):
    st.line_chart(df.set_index(selected_xaxis)[selected_yaxis])
    st.bar_chart(df.set_index(selected_xaxis)[selected_yaxis])


