import numpy as np
from openfermion.chem import MolecularData
from calculations import run_hf
r1 = 0
r2 = 0
theta = 0
geometry = []
Water_Geometries = []
angles = [0, np.pi / 2, np.pi]
for i in np.linspace(1, 3, 3):
    for j in np.linspace(1, 3, 3):
        for k in angles:
            r1 = i
            r2 = j
            theta = k
            geometry = (
                [
                    [["r1", r1], ["r2", r2], ["theta", theta]],
                    ["O", [0.0, 0.0, 0.0]],
                    ["H", [r1, 0.0, 0.0]],
                    ["H", [r2 * np.cos(theta), r2 * np.sin(theta), 0.0]],
                ],
            )
            Water_Geometries.append(geometry)
print(Water_Geometries)


def generate_cartesian_triamotic_geometry(r1, r2, angle, atoms):
    pass

    # return geometry
    # [
    #         ["H", [0.0, 0.0, 0.0]],
    #         ["H", [0.90, 0.0, 0.0]],
    #         ["H", [0.45, 0.779422863, 0.0]],
    #     ]


def generate_molecular_data_object(r1, r2, angle, atoms, basis, multiplicity, charge):
    geometry = generate_cartesian_triamotic_geometry(r1, r2, angle, atoms)
    return MolecularData(
        geometry=geometry, basis=basis, multiplicity=multiplicity, charge=charge
    )


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