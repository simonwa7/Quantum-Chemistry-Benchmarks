import json

datafilename = "basis_sets_data.json"
with open(datafilename, "r") as f:
    basis_data = json.loads(f.read())

datafilename = "geometries_data.json"
with open(datafilename, "r") as f:
    geometry_data = json.loads(f.read())

all_data = {**basis_data, **geometry_data}


atomic_number_map = {
    "H": 1,
    "He": 2,
    "Li": 3,
    "Be": 4,
    "B": 5,
    "C": 6,
    "N": 7,
    "O": 8,
    "F": 9,
    "Ne": 10,
    "Na": 11,
    "Mg": 12,
    "Al": 13,
    "Si": 14,
    "P": 15,
    "S": 16,
    "Cl": 17,
    "Ar": 18,
    "K": 19,
    "Ca": 20,
    "Sc": 21,
    "Ti": 22,
    "V": 23,
    "Cr": 24,
    "Mn": 25,
    "Fe": 26,
    "Co": 27,
    "Ni": 28,
    "Cu": 29,
    "Zn": 30,
    "Ga": 31,
    "Ge": 32,
    "As": 33,
    "Se": 34,
    "Br": 35,
    "Kr": 36,
    "Rb": 37,
}


for molecule_name in all_data.keys():
    for configuration in all_data[molecule_name]:
        largest_atomic_number = max(
            [atomic_number_map[atom[0]] for atom in configuration["geometry"]]
        )
        configuration["largest_atomic_number"] = largest_atomic_number

with open("all_data.json", "w") as f:
    f.write(json.dumps(all_data))
