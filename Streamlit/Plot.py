import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff

st.header('1. Altair Scatter Plot')
chart_data = pd.DataFrame(np.random.randn(500,5), columns = ['a','b','c','d','e'])
chart = alt.Chart(chart_data).mark_circle().encode(x = 'a' , y = 'b', size = 'c',
        tooltip = ['a','b','c','d','e'])
st.altair_chart(chart)


st.header('2. Interactive Charts')
st.subheader('2.1 Line Chart')
df = pd.read_csv('lang_data.csv')
lang_list = df.columns.tolist()
lang_choices = st.multiselect('Choose your language', lang_list)
new_df = df[lang_choices]
st.line_chart(new_df)

st.subheader('2.2 Area Chart')
st.area_chart(new_df)

st.header('3. Data Visualisation with Plotly')
st.subheader('3.1 Displaying the dataset')
df = pd.read_csv('tips.csv')
st.dataframe(df.head())

st.subheader('3.2 Pie Chart')
fig = px.pie(df, values = 'total_bill', names = 'day')
st.plotly_chart(fig)

st.subheader('3.3 Pie Chart with Multiple Parameters')
fig = px.pie(df, values = 'total_bill', names = 'day', opacity = .7,
            color_discrete_sequence = px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.subheader('3.4 Histogram')
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1,x2,x3]
group_labels = ['Group - 1', 'Group - 2', 'Group - 3']
fig = ff.create_distplot(hist_data, group_labels, bin_size = [.1,.25,.5])

st.plotly_chart(fig)
