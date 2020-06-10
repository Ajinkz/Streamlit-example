# streamlit_example
Streamlit’s open-source app framework is the easiest way to create beautiful apps 

### Hello world
```
import streamlit as st

st.title('Hello World,')
st.write("It's streamlit app")
```
![Hello streamlit](/images/0.jpg)

### Dropdown list
```
st.write("Pick up one")
keys = ['Normal','Uniform']
dist_key = st.selectbox('Which Distribution do you want?',keys)
st.write('You have chosen {}'.format(dist_key))
print(dist_key)
```
![Dropdown list](/images/1.gif)

### Tables/dataframe 
```
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

# display table
df
```
![show tables from dataframe](/images/2.JPG)

### Charts

```
# display line chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
```
![show tables from dataframe](/images/3.gif)
