import streamlit as st
st.title("User Information")

name=st.text_input("enter the name")
age = st.number_input("enter the age",min_value=1,max_value=100)
height =st.number_input("enter the height")
if st.button("display info"):
    
    st.success(f"my self {name}. I am {age} year old and my height is {height} ")
    st.success(f"name:{name}")
    st.write("name",name)