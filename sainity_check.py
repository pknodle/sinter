
from sympy import *

from sympy.physics.units import *






density_of_al = 2.70*gram/cm**3
specific_heat_al = 0.9 * joule/(gram * K)
heat_of_fusion_al = 386.9 * joule / gram
diameter_of_spot = 0.4 *mm
depth_of_spot = 0.4*mm

volume_of_spot = ((diameter_of_spot/2)**2 *3.14159) * depth_of_spot
mass_of_spot = density_of_al * volume_of_spot


# I want to raise the mass of the spot 100K in 100ms
# What power do I need?

energy_needed_to_heat = specific_heat_al * mass_of_spot * 660*K

# You need some extra energy in order to break the bonds of soilid and turn in to a liquid
# ie, the Enthalpy of fusion.
energy_needed_to_melt = heat_of_fusion_al * mass_of_spot
energy_needed = energy_needed_to_heat + energy_needed_to_melt
power_needed = energy_needed / (100*milli*seconds)


print('You will need {} '.format(power_needed))





