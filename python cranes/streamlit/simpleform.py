import streamlit as st
name = st.text_input("Enter your name",placeholder="eg. Rudra")
age = st.number_input("Enter yout age",placeholder="eg. 21")
lang = st.selectbox("Favorite language",['python','c','java','javascript'])
agree = st.checkbox("I agree to terms")

if st.button("Submit"):
    if(agree):
        st.success(f"Hello {name}, age {age}, you like {lang}")
    else:
        st.warning("please agree to terms first")