import streamlit as st
import plotly.express as px
import seaborn as sns

# Load the mtcars dataset
df = sns.load_dataset('mpg').dropna()

# Sidebar
st.sidebar.title("Controle")
x_axis = st.sidebar.selectbox("Choose X-axis:", options=df.columns)
y_axis = st.sidebar.selectbox("Choose Y-axis:", options=df.columns)
color_by = st.sidebar.selectbox("Color by:", options=df.columns)

# Main panel
st.title("Application")

# Scatter plot
fig = px.scatter(df, x=x_axis, y=y_axis, color= df[color_by].astype(object), title="mtcars Scatter Plot")
st.plotly_chart(fig)

# streamlit run app.py (executer ceci dans votre terminal, 
# de la meme maniere que vous faite pour installer 
# une nouvelle librarie)