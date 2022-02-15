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
with st.expander('Disclaimer:'):
    st.markdown('This app was developed to show a possible use case of Streamlit within an academic environment. There are a bunch of assumptions underlying it. Despite validation against selected scenarios, no one guarantees that its results are correct.')

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
        st.markdown('**Gas**')
        gas_equivalents = st.slider(
            label='Gas equivalents',
            min_value=0.0,
            max_value=20.0,
            value=10.0,
            step=0.5,
            help='Gas:Substrate stoichiometric ratio',
            key='equivalents',
        )
        gas_molecular_weight = st.number_input(
            label='Gas molecular weight [mg/mmol]',
            min_value=0.0,
            max_value=1500.0,
            value=80.0,
            step=1.0,
            help='Type in the molecular weight of the gas. Pay attention to its units.',
            key='gas-MW',
        )
        gas_mass_density = st.number_input(
            label='Gas density [mg/mL]',
            min_value=0.0,
            max_value=2.0,
            value=1.00,
            step=0.01,
            help='Type in the density of the gas. Pay attention to its units.',
            key='gas-density',
        )
        st.markdown('**Liquid**')
        liquid_flow_rate = st.slider(
            label='Flow rate of the liquid [mL/min]',
            min_value=0.0,
            max_value=20.0,
            value=10.0,
            step=0.2,
            help='Gas:Substrate stoichiometric ratio',
            key='liquid-flow-rate',
        )


else:
    with st.sidebar:
        st.subheader('Experimental parameters:')
        st.markdown('**Gas**')
        gas_equivalents = st.slider(
            label='Gas equivalents',
            min_value=0.0,
            max_value=20.0,
            value=10.0,
            step=0.5,
            help='Gas:Substrate stoichiometric ratio',
            key='equivalents',
        )
        gas_molecular_weight = st.number_input(
            label='Gas molecular weight [mg/mmol]',
            min_value=0.0,
            max_value=1500.0,
            value=80.0,
            step=1.0,
            help='Type in the molecular weight of the gas. Pay attention to its units.',
            key='gas-MW',
        )
        gas_mass_density = st.number_input(
            label='Gas density [mg/mL]',
            min_value=0.0,
            max_value=2.0,
            value=1.00,
            step=0.01,
            help='Type in the density of the gas. Pay attention to its units.',
            key='gas-density',
        )
        st.markdown('**Liquid**')

