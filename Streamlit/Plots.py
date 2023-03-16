import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt


chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['Line-1','Line-2','Line-3'])

st.header('1. Charts with random numbers')
st.subheader('1.1 Line Chart')
st.line_chart(chart_data)

st.subheader('1.2 Area Chart')
st.area_chart(chart_data)

st.subheader('1.3 Bar Chart')
st.bar_chart(chart_data)

st.header('2. Visualization with Matplotlib & Seaborn')
st.subheader('2.1 Loading the DataFrame')
df = pd.read_csv('iris.csv')
st.dataframe(df)

st.subheader('2.2 Bar Graph with Matplotlib')
fig = plt.figure(figsize = (15,8))
df['species'].value_counts().plot(kind = 'bar')
st.pyplot(fig)

st.subheader('2.3 Distribution Plot with Seaborn')
fig = plt.figure(figsize = (15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.header('3. Multiple Graphs in one columns')
col1, col2 = st.columns(2)
with col1:
    col1.header = 'KDE = False'
    fig1 = plt.figure(figsize = (5,5))
    sns.distplot(df['sepal_length'], kde = False)
    st.pyplot(fig1)
with col2:
    col2.header = 'Hist = False'
    fig2 = plt.figure(figsize = (5,5))
    sns.distplot(df['sepal_length'], hist = False)
    st.pyplot(fig2)

st.header('4. Changing Style')
col1, col2 = st.columns(2)
with col1:
    fig = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['petal_length'], hist = False)
    st.pyplot(fig)
with col2:
    fig = plt.figure()
    sns.set_theme(context = 'poster', style = 'darkgrid')
    sns.distplot(df['petal_length'], hist = False)
    st.pyplot(fig)

st.header('5. Exploring Different Graphs')
st.subheader('5.1 Scatter Plot')
fig,ax = plt.subplots(figsize = (15,8))
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)

st.subheader('5.2 Count-Plot')
fig = plt.figure(figsize = (15,8))
sns.countplot(data = df, x = 'species')
st.pyplot(fig)

st.subheader('5.3 Box-Plot')
fig = plt.figure(figsize = (15,8))
sns.boxplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(fig)

st.subheader('5.4 Violin-Plot')
fig = plt.figure(figsize = (15,8))
sns.violinplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(fig)
