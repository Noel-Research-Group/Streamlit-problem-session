"""
Streamlit-based web app for calculations of stoichiometry and stuff in
gas-liquid reactions.

D.Pintossi
2022-02-15
"""

import streamlit as st

# Streamlit page setup
st.set_page_config(
    page_title="Vial info encoder",  # label displayed by the browser
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title('Stoichiometry in Gas-Liquid reactions')
st.subheader('(in flow)')

# TODO remove when finished
st.markdown('*This Streamlit app is a work in progress*')

scenario = st.radio(
    label='Select the configuration for your Gas-Liquid flow reaction:',
    options=['Loop filling', 'Continuous flow'],
    index=0,
    key='scenario-choice',
    help='Choose the scenario corresponding to your experimental design.'
)
