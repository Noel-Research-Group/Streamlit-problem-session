"""
Streamlit-based web app for calculations of stoichiometry and stuff in
gas-liquid flow reactions.

D.Pintossi
2022-02-15
"""

import streamlit as st
from PIL import Image
from gas_equations import *

# Streamlit page setup
st.set_page_config(
    page_title="Gas-Liquid flow reaction calculator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header with logos
header = st.columns([1, 2, 1, 1, 1, 1, 1, 1, 1])
nrg_logo = Image.open('NRG Logo_300dpi_ 863x400px.png')
uva_logo = Image.open('UvA_logo.jpg')
with header[1]:
    st.image(image=nrg_logo)
with header[0]:
    st.image(image=uva_logo)

st.title('Stoichiometry in Gas-Liquid flow reactions')
st.markdown('*D.Pintossi, February 2022*')

with st.expander('Disclaimer:'):
    st.markdown('This app was developed to show a possible use case of Streamlit within an academic environment. There are a bunch of assumptions underlying it. Despite validation against selected scenarios, no one guarantees that its results are correct.')
with st.expander('Assumptions:'):
    st.markdown('- 1 bar = 1 atm (~ 1% error)')
    st.markdown('- validity of the ideal gas law')
    st.markdown('- negligible effect of geometry (e.g., shorter capillary with larger ID vs. longer one with smaller ID)')

st.markdown('___')

# Selection of the experimental design
# TODO move the selection to the sidebar (better for mobile view)
scenario = st.radio(
    label='Select the configuration for your Gas-Liquid flow reaction:',
    options=['Loop filling', 'Continuous flow'],
    index=0,
    key='scenario-choice',
    help='Choose the scenario corresponding to your experimental design.'
)

# Inputs and outputs for the two scenarios
if scenario == 'Loop filling':
    # LOOP FILLING
    with st.sidebar:
        st.subheader('Experimental parameters:')
        st.markdown('**Gas**')
        gas_equivalents = st.number_input(
            label='Gas equivalents',
            min_value=0.0,
            max_value=40.0,
            value=10.0,
            step=0.1,
            format='%f',
            help='Gas:Substrate stoichiometric ratio',
            key='equivalents',
        )
        # TODO implement selection of gas name and import of data from table
        gas_molecular_weight = st.number_input(
            label='Gas molecular weight [mg/mmol]',
            min_value=0.0,
            max_value=1500.0,
            value=80.0,
            step=1.0,
            format='%f',
            help='Type in the molecular weight of the gas. Pay attention to its units.',
            key='gas-MW',
        )
        gas_mass_density = st.number_input(
            label='Gas density [mg/mL]',
            min_value=0.0,
            max_value=5.0,
            value=1.00,
            step=0.01,
            format='%f',
            help='Type in the density of the gas. Pay attention to its units.',
            key='gas-density',
        )
        st.markdown('___')
        st.markdown('**Liquid**')
        liquid_flow_rate = st.number_input(
            label='Flow rate of the liquid [mL/min]',
            min_value=0.0,
            max_value=1.5,
            value=0.5,
            step=0.005,
            format='%f',
            help='Set the slider to the flow rate of the liquid. Mind the units.',
            key='liquid-flow-rate',
        )
        liquid_concentration = st.number_input(
            label='Concentration of substrate in solution [mmol/mL]',
            min_value=0.0,
            max_value=5.0,
            value=0.5,
            step=0.05,
            format='%f',
            help='Type in the susbtrate concentration. Mind the units.',
            key='liquid-concentration',
        )

    with st.expander('How to calculate the solution:'):
        st.markdown('With the loop filling method, the stoichiometric ratio is simply determined by the **ratio of the molar flow rates**. Pressure (and volumes) are **not** relevant.')
        st.markdown('The molar flow rate for the substrate is:')
        st.latex(
            r'''
            \dot{n}_{substrate} = c_{substrate} \cdot \dot{v}_{substrate}
            '''
        )
        st.markdown('The molar flow rate for the gas is obtained considering the number of equivalents:')
        st.latex(
            r'''
            \dot{n}_{gas} = Eq \cdot \dot{n}_{substrate}
            '''
        )
        st.markdown('The volumetric gas flow rate (STP) is:')
        st.latex(
            r'''
            \dot{v}_{gas} = \frac{MW_{gas}}{\rho_{mass, gas}} \cdot \dot{n}_{gas}
            '''
        )

    loop_filling_result = volumetric_gas_flow_rate(
        liquid_flow_rate=liquid_flow_rate,
        liquid_concentration=liquid_concentration,
        gas_equivalents=gas_equivalents,
        molecular_weight=gas_molecular_weight,
        mass_gas_density=gas_mass_density,
    )
    st.metric(
        label='Volumetric gas flow rate (STP)',
        value=f'{loop_filling_result:5.2f} mL/min',
        delta='Set this one on the MFC',
    )

else:
    # CONTINUOUS FLOW
    with st.sidebar:
        st.subheader('Experimental parameters:')
        st.markdown('**Overall**')
        residence_time = st.number_input(
            label='Residence time [min]',
            min_value=0.0,
            max_value=30.0,
            value=10.0,
            step=0.5,
            format='%f',
            help='Set the slider to the desired residence time. Mind the units.',
            key='residence-time',
        )
        reactor_volume = st.number_input(
            label='Reactor volume [mL]',
            min_value=0.0,
            max_value=15.0,
            value=5.0,
            step=0.1,
            format='%f',
            help='Type in the desired reactor volume. Mind the units.',
            key='reactor-volume',
        )
        pressure = st.number_input(
            label='Pressure (BPR + pressure drop) [bar]',
            min_value=0.0,
            max_value=45.0,
            value=9.0,
            step=1.0,
            format='%f',
            help='Type in the desired pressure. Mind the units.',
            key='pressure',
        )
        st.markdown('___')
        st.markdown('**Gas**')
        gas_equivalents = st.number_input(
            label='Gas equivalents',
            min_value=0.0,
            max_value=40.0,
            value=10.0,
            step=0.1,
            format='%f',
            help='Gas:Substrate stoichiometric ratio',
            key='equivalents',
        )
        gas_molecular_weight = st.number_input(
            label='Gas molecular weight [mg/mmol]',
            min_value=0.0,
            max_value=1500.0,
            value=80.0,
            step=1.0,
            format='%f',
            help='Type in the molecular weight of the gas. Pay attention to its units.',
            key='gas-MW',
        )
        gas_mass_density = st.number_input(
            label='Gas density [mg/mL]',
            min_value=0.0,
            max_value=5.0,
            value=1.80,
            step=0.01,
            format='%f',
            help='Type in the density of the gas. Pay attention to its units.',
            key='gas-density',
        )
        st.markdown('___')
        st.markdown('**Liquid**')
        liquid_concentration = st.number_input(
            label='Concentration of substrate in solution [mmol/mL]',
            min_value=0.0,
            max_value=5.0,
            value=0.1,
            step=0.05,
            format='%f',
            help='Type in the susbtrate concentration. Mind the units.',
            key='liquid-concentration',
        )

    with st.expander('How to calculate the solution:'):
        st.markdown(
            'With the continuous flow method, the stoichiometric ratio is still determined by the **ratio of the molar flow rates**, but the **sum of the volumetric flow rates** will determine the residence time.')
        st.markdown('The total flow rate is:')
        st.latex(
            r'''
            \dot{v}_{total} = \dot{v}_{gas, p} + \dot{v}_{substrate} = \frac{\dot{v}_{gas, STP}}{p} + \dot{v}_{substrate}
            '''
        )
        st.markdown(
            'The molar flow rates determine the stoichiometric ratio:')
        st.latex(
            r'''
            \dot{n}_{substrate} = c_{substrate} \cdot \dot{v}_{substrate}
            '''
        )
        st.latex(
            r'''
            \dot{n}_{gas} = Eq \cdot \dot{n}_{substrate} = Eq \cdot c_{substrate} \cdot \dot{v}_{substrate}
            '''
        )
        st.latex(
            r'''
            \dot{v}_{gas} = \frac{MW_{gas}}{\rho_{mass, gas}} \cdot \dot{n}_{gas} = \frac{MW_{gas}}{\rho_{mass, gas}} \cdot Eq \cdot c_{substrate} \cdot \dot{v}_{substrate}
            '''
        )
        st.markdown('The two conditions give the following linear system:')
        st.latex(
            r'''
            \begin{equation}
                \begin{cases}
                    \frac{1}{p}\dot{v}_{gas, STP} + \dot{v}_{substrate} = \dot{v}_{total} \\
                    \dot{v}_{gas, STP} - \frac{MW_{gas}}{\rho_{mass, gas}} \cdot Eq \cdot c_{substrate} \cdot \dot{v}_{substrate} = 0
                \end{cases}
            \end{equation}
            '''
        )
        st.markdown('The system can be expressed in matrix notation and solved with `scipy.linalg.solve`:')
        st.latex(
            r'''
            \begin{bmatrix}
                \frac{1}{p} & 1 \\
                1 & - \frac{MW_{gas}}{\rho_{mass, gas}} \cdot Eq \cdot c_{substrate}
            \end{bmatrix}
            \cdot
            \begin{bmatrix}
                \dot{v}_{gas, STP} \\
                \dot{v}_{substrate}
            \end{bmatrix}
            =
            \begin{bmatrix}
                \dot{v}_{total} \\
                0
            \end{bmatrix}
            '''
        )

    gas_flow, liquid_flow = volumetric_gas_and_liquid_flow_rates(
        pressure=pressure,
        gas_equivalents=gas_equivalents,
        liquid_concentration=liquid_concentration,
        gas_molecular_weight=gas_molecular_weight,
        gas_mass_density=gas_mass_density,
        residence_time=residence_time,
        reactor_volume=reactor_volume,
    )
    columns = st.columns(4)
    with columns[0]:
        st.metric(
            label='Volumetric gas flow rate (STP)',
            value=f'{gas_flow:5.3f} mL/min',
            delta='Set this one on the MFC',
        )
    with columns[1]:
        st.metric(
            label=f'Volumetric gas flow rate at {pressure} bar',
            value=f'{gas_flow / pressure:5.3f} mL/min'
        )
    with columns[2]:
        st.metric(
            label='Volumetric liquid flow rate',
            value=f'{liquid_flow:5.3f} mL/min',
            delta='Set this one on the pump',
        )
    with columns[3]:
        GL_ratio = gas_flow / (pressure * liquid_flow)
        st.metric(
            label=f'Gas : Liquid ratio (vol.) at {pressure} bar',
            value=f'{GL_ratio:3.1f} : 1',
        )

