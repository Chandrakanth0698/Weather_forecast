import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text_input, slider, selection box
st.title("Weather Forcast App")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days to forcast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

# get temperature/ sky data
if place:
    try:
        filtered_content = get_data(place, days, API_key=st.secrets["API_key"])
        dates = [observation["dt_txt"] for observation in filtered_content]
        st.subheader(f"{option} for the next {days} dapip freeze > requirements.txtys in {place} for every 3 hours.")
        if option == "Temperature":
            temperatures = [observation["main"]["temp"]/10 for observation in filtered_content]
            print(temperatures)
            # create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y":"Temperature (C)"})
            st.plotly_chart(figure)
        else:
            sky_condition = [observation["weather"][0]["main"] for observation in filtered_content]
            print(sky_condition)
            image_path = [f"images/{image.lower()}.png" for image in sky_condition]
            st.image(image_path, width=100, caption=sky_condition)
    except KeyError:
        st.info("Please enter correct city name")
