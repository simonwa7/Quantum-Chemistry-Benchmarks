import json
import matplotlib.pyplot as plt

datafilename = "data/geometries_data.json"
with open(datafilename, "r") as f:
    data = json.loads(f.read())


hf_errors = []
mp2_errors = []
cisd_errors = []
ccsd_errors = []
molecule_names = []
colors = []
color = 0
for molecule_name, molecule_data in data.items():

    for configuration in molecule_data:
        if configuration.get("fci", False):
            fci_energy = configuration["fci"]["energy"]
            molecule_names.append(molecule_name)
            colors.append(color)
            hf_errors.append(abs(configuration["scf"]["energy"] - fci_energy))
            mp2_errors.append(abs(configuration["mp2"]["energy"] - fci_energy))
            cisd_errors.append(abs(configuration["cisd"]["energy"] - fci_energy))
            ccsd_errors.append(abs(configuration["ccsd"]["energy"] - fci_energy))

    color += 1


fig, axes = plt.subplots(
    3,
    2,
    figsize=(18, 12),
)

plt.rc("font", size=10)  # controls default text size
plt.rc("axes", titlesize=10)  # fontsize of the title
plt.rc("axes", labelsize=10)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=10)  # fontsize of the x tick labels
plt.rc("ytick", labelsize=10)  # fontsize of the y tick labels
plt.rc("legend", fontsize=10)  # fontsize of the legend

from itertools import combinations

plt.suptitle("Errors from Classical Chemistry Approximation Methods")
for i, (method1, method2) in enumerate(
    combinations(
        [
            {
                "method": "HF",
                "errors": hf_errors,
            },
            {
                "method": "CCSD",
                "errors": ccsd_errors,
            },
            {
                "method": "CISD",
                "errors": cisd_errors,
            },
            {
                "method": "MP2",
                "errors": mp2_errors,
            },
        ],
        2,
    )
):
    ax = axes[int(i % 3)][int(i / 3)]
    ax.scatter(method1["errors"], method2["errors"], c=colors)
    ax.set_xlabel("Error from {}".format(method1["method"]))
    ax.set_ylabel("Error from {}".format(method2["method"]))
plt.savefig("figures/classical_method_errors.pdf", dpi=300)
