import streamlit as st
st.header("Columnns Layout")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Temperature", "36 °C", "+2 °C")
with col2:
    st.metric("Humidity", "72%", "-5%")
with col3:
    st.metric("Voltage","5.02V","+0.02V")