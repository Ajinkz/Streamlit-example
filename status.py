import streamlit as st
import time


# initialise placeholder
my_placeholder = st.empty()
# assign value
my_placeholder.text("Loading ...")
# progress bar
my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

# update value after some event
my_placeholder.text("Loading completed !")


# # display code
# with st.echo():
#     with st.echo():
#         st.write('This code will be printed')

with st.echo():
    # errors
    st.error('This is an error')

with st.echo():
    # wwarnings
    st.warning('This is a warning')

with st.echo():
    # info
    st.info('This is a purely informational message')

with st.echo():
    # success
    st.success('This is a success message!')

with st.echo():
    # exceptions
    e = RuntimeError('This is an exception of type RuntimeError')
    st.exception(e)

with st.echo():
    # help
    st.help(time)

# spinner
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('The End!')

# Balloons
st.balloons()