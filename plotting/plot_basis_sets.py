import json
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys

datafilename = "data/basis_sets_data.json"
with open(datafilename, "r") as f:
    data = json.loads(f.read())

# qubit_counts = {
#     "H2_sto-3g_singlet": 4,
#     "H2_3-21g_singlet": 8,
#     "H2_6-31g_singlet": 8,
#     "H2_6-31+g_singlet": 8,
#     "H2_6-31++g_singlet": 12,
#     "H2_6-31g*_singlet": 8,
#     "H2_6-31+g*_singlet": 8,
#     "H2_6-31++g*_singlet": 12,
#     "H2_6-311g_singlet": 12,
#     "H2_6-311+g_singlet": 12,
#     "H2_6-311++g_singlet": 16,
#     "H2_6-311g*_singlet": 12,
#     "H2_6-311+g*_singlet": 12,
#     "H2_6-311++g*_singlet": 16,
#     "H2_6-311g**_singlet": 24,
#     "H2_6-311+g**_singlet": 24,
#     "H2_6-311++g**_singlet": 28,
#     "H2_def2-SV(P)_singlet": 8,
#     "H2_def2-SVP_singlet": 20,
#     "H2_def2-SVPD_singlet": 32,
#     "H2_def2-TZVP_singlet": 24,
#     "H2_def2-TZVPD_singlet": 36,
#     "H2_def2-TZVPP_singlet": 56,
#     "H2_def2-TZVPPD_singlet": 68,
#     "H2_def2-QZVP_singlet": 120,
#     "H2_def2-QZVPD_singlet": 132,
#     "H2_def2-QZVPP_singlet": 120,
#     "H2_def2-QZVPPD_singlet": 132,
#     "H1-Li1_sto-3g_singlet": 12,
#     "H1-Li1_6-31g_singlet": 22,
#     "H1-Li1_6-31+g_singlet": 30,
#     "H1-Li1_6-31++g_singlet": 32,
#     "H1-Li1_6-31g*_singlet": 34,
#     "H1-Li1_6-31+g*_singlet": 42,
#     "H1-Li1_6-31++g*_singlet": 44,
#     "H1-Li1_6-311g_singlet": 32,
#     "H1-Li1_6-311+g_singlet": 40,
#     "H1-Li1_6-311++g_singlet": 42,
#     "H1-Li1_6-311g*_singlet": 42,
#     "H1-Li1_6-311+g*_singlet": 50,
#     "H1-Li1_6-311++g*_singlet": 52,
#     "H1-Li1_6-311g**_singlet": 48,
#     "H1-Li1_6-311+g**_singlet": 56,
#     "H1-Li1_6-311++g**_singlet": 58,
#     "H1-Li1_def2-SV(P)_singlet": 22,
#     "H1-Li1_def2-SVP_singlet": 28,
#     "H1-Li1_def2-SVPD_singlet": 40,
#     "H1-Li1_def2-TZVP_singlet": 40,
#     "H1-Li1_def2-TZVPD_singlet": 52,
#     "H1-Li1_def2-TZVPP_singlet": 66,
#     "H1-Li1_def2-TZVPPD_singlet": 78,
#     "H1-Li1_def2-QZVP_singlet": 130,
#     "H1-Li1_def2-QZVPD_singlet": 136,
#     "H1-Li1_def2-QZVPP_singlet": 130,
#     "H1-Li1_def2-QZVPPD_singlet": 136,
#     "H2-Be1_3-21g_singlet": 26,
#     "H2-Be1_6-31g_singlet": 26,
#     "H2-Be1_6-31+g_singlet": 34,
#     "H2-Be1_6-31++g_singlet": 38,
#     "H2-Be1_6-31g*_singlet": 38,
#     "H2-Be1_6-31+g*_singlet": 46,
#     "H2-Be1_6-31++g*_singlet": 50,
#     "H2-Be1_6-311g_singlet": 38,
#     "H2-Be1_6-311+g_singlet": 46,
#     "H2-Be1_6-311++g_singlet": 50,
#     "H2-Be1_6-311g*_singlet": 48,
#     "H2-Be1_6-311+g*_singlet": 56,
#     "H2-Be1_6-311++g*_singlet": 60,
#     "H2-Be1_6-311g**_singlet": 60,
#     "H2-Be1_6-311+g**_singlet": 68,
#     "H2-Be1_6-311++g**_singlet": 72,
#     "H2-Be1_def2-SV(P)_singlet": 26,
#     "H2-Be1_def2-SVP_singlet": 38,
#     "H2-Be1_def2-SVPD_singlet": 56,
#     "H2-Be1_def2-TZVP_singlet": 62,
#     "H2-Be1_def2-TZVPD_singlet": 80,
#     "H2-Be1_def2-TZVPP_singlet": 94,
#     "H2-Be1_def2-TZVPPD_singlet": 112,
#     "H2-Be1_def2-QZVP_singlet": 192,
#     "H2-Be1_def2-QZVPD_singlet": 204,
#     "H2-Be1_def2-QZVPP_singlet": 192,
#     "H2-Be1_def2-QZVPPD_singlet": 204,
#     "H2-O1_3-21g_singlet": 26,
#     "H2-O1_6-31g_singlet": 26,
#     "H2-O1_6-31+g_singlet": 34,
#     "H2-O1_6-31++g_singlet": 38,
#     "H2-O1_6-31g*_singlet": 38,
#     "H2-O1_6-31+g*_singlet": 46,
# }

MOLECULE = sys.argv[1]
print(MOLECULE)
molecule_names = []
basis_sets = []
numbers_of_qubits = []
methods = []
errors = []
times = []

for molecule_name, molecule_data in data.items():
    name = molecule_name[: molecule_name.find("_")]
    basis_set = molecule_name[molecule_name.find("_") + 1 : molecule_name.rfind("_")]

    for configuration in molecule_data:
        # fci_energy = configuration["fci"]["energy"]
        fci_energy = data[MOLECULE + "_def2-TZVPPD_singlet"][0]["fci"]["energy"]

        for method in ["hf", "mp2", "cisd", "ccsd"]:

            molecule_names.append(name)
            basis_sets.append(basis_set)
            numbers_of_qubits.append(configuration["number_of_qubits"])
            methods.append(method)
            if method == "hf":
                method = "scf"
            error = abs(configuration[method]["energy"] - fci_energy)
            assert error >= 0.0
            errors.append(error)
            times.append(configuration[method]["cpu_time"])

data = {
    "Molecule": molecule_names,
    "Basis Set": basis_sets,
    "Number of Qubits": numbers_of_qubits,
    "Method": methods,
    "Error": errors,
    "Time": times,
}

data = pd.DataFrame(data)

plt.rc("font", size=10)  # controls default text size
plt.rc("axes", titlesize=10)  # fontsize of the title
plt.rc("axes", labelsize=10)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=10)  # fontsize of the x tick labels
plt.rc("ytick", labelsize=10)  # fontsize of the y tick labels
plt.rc("legend", fontsize=10)  # fontsize of the legend

H2O_data = data[data["Molecule"] == MOLECULE]
sns.scatterplot(data=H2O_data, x="Number of Qubits", y="Error", hue="Method")
plt.yscale("log")
plt.title(MOLECULE)
plt.legend(loc="upper right")
plt.savefig(MOLECULE + ".pdf", dpi=300)
