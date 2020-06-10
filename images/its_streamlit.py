import streamlit as st
import pandas as pd
import numpy as np
import time

# ---------------------------1-------------------------------------
st.title('Hello World, its streamlit')
st.write('Pick an option')
keys = ['Normal','Uniform']
dist_key = st.selectbox('Which Distribution do you want?',keys)
st.write('You have chosen {}'.format(dist_key))

#----------------------------2----------------------------------
