"""
Functions to be used in the stoichiometry calculations

D.Pintossi
2022-02-15
"""

import numpy as np
from scipy.linalg import solve


# LOOP FILLING
def volumetric_gas_flow_rate(
        liquid_flow_rate, liquid_concentration,
        gas_equivalents, molecular_weight, mass_gas_density,
):
    """Calculation of the volumetric gas flow ratio to obtain a desired
    stoichiometry in the LOOP FILLING configuration.

    :param liquid_flow_rate: float
        Liquid flow rate [mL/min]
    :param liquid_concentration: float
        Concentration of the substrate in solution [mmol/mL]
    :param gas_equivalents: float
        Gas:Substrate stoichiometric ratio [-]
    :param molecular_weight: float
        Molecular weight of the gas [mg/mmol]
    :param mass_gas_density: float
        Density of the gas [mg/mL]
    :return: float
        Volumetric gas flow rate [mL/min]
    """
    return (molecular_weight / mass_gas_density) \
             * gas_equivalents * liquid_concentration * liquid_flow_rate


# CONTINUOUS FLOW
def volumetric_gas_and_liquid_flow_rates(
        pressure, gas_equivalents, liquid_concentration,
        gas_molecular_weight, gas_mass_density,
        residence_time, reactor_volume
):
    """Calculation of the volumetric gas and liquid flow rates at a given
    pressure, stoichiometry, and residence time (CONTINUOUS FLOW configuration).

    :param pressure: float
        Pressure inside the capillary (BPR + pressure drop)
    :param gas_equivalents: float
        Gas:Substrate stoichiometric ratio [-]
    :param liquid_concentration: float
        Concentration of the substrate in solution [mmol/mL]
    :param gas_molecular_weight: float
        Molecular weight of the gas [mg/mmol]
    :param gas_mass_density: float
        Density of the gas [mg/mL]
    :param residence_time: float
        Desired residence time [min]
    :param reactor_volume: float
        Inner volume of the reactor [mL]
    :return: tuple
        Volumetric gas flow rate [mL/min], volumetric liquid flow rate [mL/min]
    """
    # Setting up the system of linear equations (matrix formulation)
    # 1. constraint on flow rates
    # 2. stoichiometry
    a11 = 1 / pressure  # 1% error by considering 1 atm = 1 bar
    a22 = - gas_molecular_weight * gas_equivalents * liquid_concentration \
            / gas_mass_density
    A = np.array([[a11, 1], [1, a22]])

    b1 = reactor_volume / residence_time
    b = np.array([[b1], [0]])

    x = solve(A, b)

    gas_flow_rate_STP = x[0][0]
    liquid_flow_rate = x[1][0]

    return gas_flow_rate_STP, liquid_flow_rate
