import numpy as np
from openfermion.chem import MolecularData
from calculations import run_fci, run_hf


def generate_cartesian_triamotic_geometry(radius1, radius2, angle, atoms):
    geometry =  [
            [atoms[0], [0.0, 0.0, 0.0]],
            [atoms[1], [radius1, 0.0, 0.0]],
            [atoms[2], [radius2 * np.cos(angle), radius2 * np.sin(angle), 0.0]],
        ]

    return  geometry


def generate_molecular_data_object(r1, r2, angle, atoms, basis, multiplicity, charge):
    geometry = generate_cartesian_triamotic_geometry(r1, r2, angle, atoms)
    return MolecularData(
        geometry=geometry, basis=basis, multiplicity=multiplicity, charge=charge
    )


# geometry = generate_cartesian_triamotic_geometry(0.1, .3, np.pi/3, ["O","H","H"])
# molecule = MolecularData(
#     geometry=geometry,
#     basis="sto-3g",
#     multiplicity=1,
#     charge=0
# )
# print(molecule.geometry)
# print(molecule.)
r1 = 0
r2 = 0
theta = 0
geometry = []
water_molecules = []
angles = [0, np.pi / 2, np.pi]
number_of_angles= 100
angles = [(i/number_of_angles)*2*np.pi for i in range(number_of_angles)]
for i in np.linspace(1, 3, 4):
    for j in np.linspace(1, 3, 4):
        for k in angles:
            r1 = i
            r2 = j
            theta = k
            water_molecules.append(generate_molecular_data_object(r1, r2, theta, ["O","H","H"], "sto-3g", 1, 0))

for molecule in water_molecules:
    print(molecule.geometry)
    print(molecule.basis)
    print(molecule.multiplicity)
    print(molecule.charge)
    print(molecule.scf_energy)

print(len(water_molecules))

# TODO: Loop over water molecules and run FCI and run HF
# To figure this out, look insides caluclations.py at how run_fci and run_hf are defined. print out energies and errors (abs(FCI - HF))
#print("FCI Energy: {}, HF Energy: {}, Error: {}".format(fci_energy, hf_energy, error))
# Stretch Goal #1: Add, Commit this file to GitHub on your branch when the above is done
# Stretch Goals: Do this for _all_ methods (except noncontextual ones) defined in calculations.py, present data in a way that looks nice

# all_molecular_data_objects = []
# all_cyclindrical_coordinates = []
# atoms = []
# basis = ""
# multiplicity = 0
# charge = 0
# for r1 in r1s:
#     for r2 in r2s:
#         for angle in angles:
#             cyclindrical_coordinates = {"r1": r1, "r2": r2, "angle": angle}
#             all_cyclindrical_coordinates.append(cyclindrical_coordinates)
#             all_molecular_data_objects.append(
#                 generate_molecular_data_object(
#                     r1, r2, atoms, basis, multiplicity, charge
#                 )
#             )