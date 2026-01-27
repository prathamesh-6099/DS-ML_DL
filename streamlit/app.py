import streamlit as st
import pandas as pd
import numpy as np

# Tittle of the application
st.title(" Hello streamlit ")

#Display a simple text
st.write(" This is simple Text")

# Create a simple Data frames

df=pd.DataFrame({
    'first column': [1,2,3,4],
    'second column' : [10,20,30,40]
})

# Display The Dataframe
st.write("Here is the Dataframe ")
st.write(df)

#Create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)