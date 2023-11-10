import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forcast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5, help="Select the number of days to forcast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}.")
figure = px.line()
st.plotly_chart(figure)
