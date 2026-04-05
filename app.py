import streamlit as st
from datetime import datetime as dt
from simulator import monte_carlo_qualifying
from plotting import position_probability_plot, expected_position

st.title('F1 Qualifying Simulator')
st.text('This app uses Monte Carlo simulation to simulate Formula 1 Qualifying sessions.')

year = st.number_input("Year", min_value=2018, max_value=dt.now().year, value=2025)
gp = st.text_input("Grand Prix")
n = st.number_input("Number of simulations", min_value=1, max_value=5000, value=500)
pos = st.number_input("Position", min_value=1, max_value=22, value=1)
driver = st.text_input("Driver")




run = st.button("Run Simulation")

if run:
    st.write("Running simulation...")

    st.dataframe(monte_carlo_qualifying(gp, year, n))

    fig = position_probability_plot(gp, year, pos, n)

    st.pyplot(fig, use_container_width=True)

    fig = expected_position(gp, year, driver, n)

    st.pyplot(fig, use_container_width=True)