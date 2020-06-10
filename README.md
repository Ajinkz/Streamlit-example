[Streamlit example website](https://ajinkz.github.io/Streamlit-example/)

# Streamlit example
[Streamlit](https://www.streamlit.io/) is a open-source app framework is the easiest way to create beautiful apps 

### Hello world
```python
import streamlit as st

st.title('Hello World,')
st.write("It's streamlit app")
```
![Hello streamlit](/images/0.jpg)

### Dropdown list
```python
st.write("Pick up one")
keys = ['Normal','Uniform']
dist_key = st.selectbox('Which Distribution do you want?',keys)
st.write('You have chosen {}'.format(dist_key))
print(dist_key)
```
![Dropdown list](/images/1.gif)

### Tables/dataframe 
```python
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

# display table
df
```
![show tables from dataframe](/images/2.JPG)

### Charts
```python
# display line chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
```
![show tables from dataframe](/images/3.gif)

### Maps
```python
# map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
```
![show maps](/images/4_map.gif)

### Checkbox/sidebar widgets
```python
# checkboxes
if st.checkbox('Show chart'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

# selectbox
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# sidebar widget
option1 = st.sidebar.selectbox(
    'Which number do you like best?',
     df['second column'])

'You selected:', option1
```
![show checkbox/sidebar widgets](/images/5_checkbox_dropdown.gif)

### Animation
```python
# animate
progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(100):
    # Update progress bar.
    progress_bar.progress(i)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.1)

status_text.text('Done!')
st.balloons()
```
![Display animation](/images/5_animate.gif)


## Reference
* [Official site](https://www.streamlit.io/)
* [Docs](https://docs.streamlit.io/en/latest/)

## Deployment
* [AWS](https://mlwhiz.com/blog/2020/02/22/streamlitec2/)
* [Heroku](https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83)

## about me

<div class="LI-profile-badge"  data-version="v1" data-size="medium" data-locale="en_US" data-type="vertical" data-theme="dark" data-vanity="ajinkyanpathak"><a class="LI-simple-link" href='https://in.linkedin.com/in/ajinkyanpathak?trk=profile-badge'>Ajinkya Pathak</a></div>
