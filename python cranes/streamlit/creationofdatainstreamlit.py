import streamlit as st
import pandas as pd

data = pd.DataFrame({
    "Day":["Mon","Tue","Wed","thu","Fri"],
    "Sales":[120,95,150,200,175],
    "Returns":[10,5,20,15,8]}
    )

st.header("Sales Data")
st.dataframe(data)
st.line_chart(data.set_index("Day"))
st.bar_chart(data.set_index("Day")["Sales"])