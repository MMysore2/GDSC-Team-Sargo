import streamlit as st 
import pandas as pd
import numpy as np


st.write("Hello World! I am currently learning Streamlit.")

st.write("Here's our first attempt at using data to create a table:")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

""""""
""""""
st.write("Let's create a data frame and change its formatting with a \
         Pandas Styler object. In this example, you'll use Numpy to \
         generate a random sample, and the st.dataframe() method to draw \
         an interactive table.")

dataframe = pd.DataFrame(
    np.random.randn(10,20), 
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

