import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days you wish to view Weather data for")
option = st.selectbox("Select data to view",("Temperature","Sky"))
st.title(f"{option} for the next {days} in {place}")