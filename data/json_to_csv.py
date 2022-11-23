import json
import pandas as pd

datafilename = "basis_sets_data.json"
with open(datafilename, "r") as f:
    data = json.loads(f.read())

qubit_counts = {
    "H2_sto-3g_singlet": 4,
    "H2_3-21g_singlet": 8,
    "H2_6-31g_singlet": 8,
    "H2_6-31+g_singlet": 8,
    "H2_6-31++g_singlet": 12,
    "H2_6-31g*_singlet": 8,
    "H2_6-31+g*_singlet": 8,
    "H2_6-31++g*_singlet": 12,
    "H2_6-311g_singlet": 12,
    "H2_6-311+g_singlet": 12,
    "H2_6-311++g_singlet": 16,
    "H2_6-311g*_singlet": 12,
    "H2_6-311+g*_singlet": 12,
    "H2_6-311++g*_singlet": 16,
    "H2_6-311g**_singlet": 24,
    "H2_6-311+g**_singlet": 24,
    "H2_6-311++g**_singlet": 28,
    "H2_def2-SV(P)_singlet": 8,
    "H2_def2-SVP_singlet": 20,
    "H2_def2-SVPD_singlet": 32,
    "H2_def2-TZVP_singlet": 24,
    "H2_def2-TZVPD_singlet": 36,
    "H2_def2-TZVPP_singlet": 56,
    "H2_def2-TZVPPD_singlet": 68,
    "H2_def2-QZVP_singlet": 120,
    "H2_def2-QZVPD_singlet": 132,
    "H2_def2-QZVPP_singlet": 120,
    "H2_def2-QZVPPD_singlet": 132,
    "H1-Li1_sto-3g_singlet": 12,
    "H1-Li1_6-31g_singlet": 22,
    "H1-Li1_6-31+g_singlet": 30,
    "H1-Li1_6-31++g_singlet": 32,
    "H1-Li1_6-31g*_singlet": 34,
    "H1-Li1_6-31+g*_singlet": 42,
    "H1-Li1_6-31++g*_singlet": 44,
    "H1-Li1_6-311g_singlet": 32,
    "H1-Li1_6-311+g_singlet": 40,
    "H1-Li1_6-311++g_singlet": 42,
    "H1-Li1_6-311g*_singlet": 42,
    "H1-Li1_6-311+g*_singlet": 50,
    "H1-Li1_6-311++g*_singlet": 52,
    "H1-Li1_6-311g**_singlet": 48,
    "H1-Li1_6-311+g**_singlet": 56,
    "H1-Li1_6-311++g**_singlet": 58,
    "H1-Li1_def2-SV(P)_singlet": 22,
    "H1-Li1_def2-SVP_singlet": 28,
    "H1-Li1_def2-SVPD_singlet": 40,
    "H1-Li1_def2-TZVP_singlet": 40,
    "H1-Li1_def2-TZVPD_singlet": 52,
    "H1-Li1_def2-TZVPP_singlet": 66,
    "H1-Li1_def2-TZVPPD_singlet": 78,
    "H1-Li1_def2-QZVP_singlet": 130,
    "H1-Li1_def2-QZVPD_singlet": 136,
    "H1-Li1_def2-QZVPP_singlet": 130,
    "H1-Li1_def2-QZVPPD_singlet": 136,
    "H2-Be1_3-21g_singlet": 26,
    "H2-Be1_6-31g_singlet": 26,
    "H2-Be1_6-31+g_singlet": 34,
    "H2-Be1_6-31++g_singlet": 38,
    "H2-Be1_6-31g*_singlet": 38,
    "H2-Be1_6-31+g*_singlet": 46,
    "H2-Be1_6-31++g*_singlet": 50,
    "H2-Be1_6-311g_singlet": 38,
    "H2-Be1_6-311+g_singlet": 46,
    "H2-Be1_6-311++g_singlet": 50,
    "H2-Be1_6-311g*_singlet": 48,
    "H2-Be1_6-311+g*_singlet": 56,
    "H2-Be1_6-311++g*_singlet": 60,
    "H2-Be1_6-311g**_singlet": 60,
    "H2-Be1_6-311+g**_singlet": 68,
    "H2-Be1_6-311++g**_singlet": 72,
    "H2-Be1_def2-SV(P)_singlet": 26,
    "H2-Be1_def2-SVP_singlet": 38,
    "H2-Be1_def2-SVPD_singlet": 56,
    "H2-Be1_def2-TZVP_singlet": 62,
    "H2-Be1_def2-TZVPD_singlet": 80,
    "H2-Be1_def2-TZVPP_singlet": 94,
    "H2-Be1_def2-TZVPPD_singlet": 112,
    "H2-Be1_def2-QZVP_singlet": 192,
    "H2-Be1_def2-QZVPD_singlet": 204,
    "H2-Be1_def2-QZVPP_singlet": 192,
    "H2-Be1_def2-QZVPPD_singlet": 204,
    "H2-O1_3-21g_singlet": 26,
    "H2-O1_6-31g_singlet": 26,
    "H2-O1_6-31+g_singlet": 34,
    "H2-O1_6-31++g_singlet": 38,
    "H2-O1_6-31g*_singlet": 38,
    "H2-O1_6-31+g*_singlet": 46,
}

molecule_names = []
basis_sets = []
numbers_of_qubits = []
methods = []
errors = []
times = []
of_names = []
charges = []
multiplicities = []
geometries = []
energies = []
orbital_energies = []

for molecule_name, molecule_data in data.items():
    name = molecule_name[: molecule_name.find("_")]
    basis_set = molecule_name[molecule_name.find("_") + 1 : molecule_name.rfind("_")]

    for configuration in molecule_data:

        for method in ["hf", "mp2", "cisd", "ccsd", "fci"]:

            molecule_names.append(name)
            basis_sets.append(basis_set)
            try:
                number_of_qubits = qubit_counts[molecule_name]
            except:
                number_of_qubits = None

            numbers_of_qubits.append(number_of_qubits)
            methods.append(method)
            if method == "hf":
                method = "scf"
            # errors.append(abs(configuration[method]["energy"] - fci_energy))
            times.append(configuration[method]["cpu_time"])
            of_names.append(molecule_name)
            charges.append(configuration["charge"])
            multiplicities.append(configuration["multiplicity"])
            geometries.append(configuration["geometry"])
            energies.append(configuration[method]["energy"])
            orbital_energies.append(configuration[method]["orbital_energies"])

data = {
    "Molecule": molecule_names,
    "OF Molecule Name": of_names,
    "Geometry": geometries,
    "Charge": charges,
    "Multiplicity": multiplicities,
    "Basis Set": basis_sets,
    "Number of Qubits": numbers_of_qubits,
    "Method": methods,
    "Energy": energies,
    "Orbital Energies": orbital_energies,
    "Time": times,
}

data = pd.DataFrame(data)
data.to_csv(datafilename.replace(".json", ".csv"))
