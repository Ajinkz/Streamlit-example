from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
import time
import datetime


# Image (jpg/png)
image = Image.open('env.jpg')
st.image(image, width=None, use_column_width=False, clamp=False, channels='RGB', format='JPEG', caption='Human & Environment')

# Audio (mp3,wav,ogg)
audio_file = open('bensound-summer.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes,  format='audio/mp3', start_time=0)

# Video (mp4)
video_file = open('forest.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes, format='video/mp4', start_time=0)

# buttons
if st.button('Say hello'):
    st.write('Said "Hello"')
else:
	st.write('Goodbye')


# checkbox
agree = st.checkbox('I agree')
if agree:
	st.write('Great!')


# radio button
genre = st.radio(
    "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary','Thriller'))

if genre == 'Comedy':
    st.write('You selected comedy.')
# elif genre == 'Thriller':
#     st.write('You selected Thriller.')
else:
    st.write("You didn't select comedy.")

# select box
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


# multi-select
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)


# slider
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)


# text input
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


# numeric input
number = st.number_input('Insert a number')
st.write('The current number is ', number)


# text area
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
     ''')
st.write('Sentiment:', txt)


# date input
d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)


# time input
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)


# table
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)


# json
st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

# # file upload
# uploaded_file = st.file_uploader("Choose a CSV file")
# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
#     st.write(data)

# color picker
