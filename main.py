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

st.button(
    label='Hoi! Ik ben Benji'
)
