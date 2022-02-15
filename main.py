"""
Streamlit-based web app for calculations of stoichiometry and stuff in
gas-liquid flow reactions.

D.Pintossi
2022-02-15
"""

import streamlit as st
from gas_equations import *

# Streamlit page setup
st.set_page_config(
    page_title="Vial info encoder",  # label displayed by the browser
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title('Stoichiometry in Gas-Liquid flow reactions')
st.markdown('*D.Pintossi, February 2022*')

# TODO remove when finished
st.markdown('*This Streamlit app is a work in progress*')

scenario = st.radio(
    label='Select the configuration for your Gas-Liquid flow reaction:',
    options=['Loop filling', 'Continuous flow'],
    index=0,
    key='scenario-choice',
    help='Choose the scenario corresponding to your experimental design.'
)

if scenario == 'Loop filling':
    with st.sidebar:
        st.subheader('Experimental parameters:')
        st.number_input(
            label='Gas equivalents',
            min_value=0,
            max_value=20,
            value=10,
            step=1,
            help='Gas:Substrate stoichiometric ratio',
            key='equivalents',
        )
else:
    with st.sidebar:
        st.subheader('Experimental parameters:')
        st.number_input(
            label='Gas equivalents',
            min_value=0,
            max_value=20,
            value=10,
            step=1,
            help='Gas:Substrate stoichiometric ratio',
            key='equivalents',
        )
        st.slider()
