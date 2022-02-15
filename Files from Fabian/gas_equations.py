"""
Functions to be used in the stoichiometry calculations

D.Pintossi
2022-02-15
"""


def molar_gas_flow_rate(
        volumetric_gas_flow_rate, mass_density, molecular_weight
):
    # TODO verify measurement units and their consistency
    """Calculate the molar gas flow rate [mol s-1], which is invariant of
    temperature and pressure.

    :param volumetric_gas_flow_rate: float
        Volumetric gas flow rate [m3 s-1], dependent on temperature and pressure
    :param mass_density: float
        Density of the gas [kg m-3]
    :param molecular_weight: float
        Molecular weight of the gas [kg mol-1]
    :return: float
        Molar gas flow rate [mol s-1]
    """
    return volumetric_gas_flow_rate * mass_density / molecular_weight
