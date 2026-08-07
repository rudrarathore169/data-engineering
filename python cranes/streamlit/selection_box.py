import streamlit as st
st.title("selection box example")

names=["rathore","singh","rudra","pratap"]

selected_name = st.selectbox("choose the name",names)
if st.button("display name"):
    st.write("today my name is",selected_name)