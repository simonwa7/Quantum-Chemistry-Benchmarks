import json
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys

datafilename = "data/basis_sets_data.json"
with open(datafilename, "r") as f:
    data = json.loads(f.read())

MOLECULE = sys.argv[1]
molecule_names = []
basis_sets = []
numbers_of_qubits = []
methods = []
errors = []
times = []

for molecule_name, molecule_data in data.items():
    name = molecule_name[: molecule_name.find("_")]
    basis_set = molecule_name[molecule_name.find("_") + 1 : molecule_name.rfind("_")]

    if MOLECULE == name:

        for configuration in molecule_data:
            fci_energy = data[MOLECULE + "_def2-TZVPPD_singlet"][0]["fci"]["energy"]

            for method in ["hf", "mp2", "cisd", "ccsd"]:
                if method == "hf":
                    method = "scf"
                if configuration.get(method, False):
                    molecule_names.append(name)
                    basis_sets.append(basis_set)
                    numbers_of_qubits.append(configuration["number_of_qubits"])
                    methods.append(method)
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
plt.legend(loc="lower left")
plt.savefig("figures/" + MOLECULE + ".pdf", dpi=300)
