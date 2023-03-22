from utils import get_method_errors_and_labels
import json

import matplotlib.pyplot as plt

data_filename = "/Users/williamsimon/Desktop/Research/QuantumChemistryBenchmarks/data/geometries_data.json"
label = "number_of_qubits"

with open(data_filename, "r") as f:
    data = json.loads(f.read())

errors = []
labels = []
colors = []
for i, method in enumerate(["scf", "mp2", "cisd", "ccsd", "nc_SingleSweep_magnitude"]):
    (
        method_errors,
        method_labels,
    ) = get_method_errors_and_labels(data, method, label)
    errors += method_errors
    labels += method_labels
    colors += [i for _ in method_errors]

plt.rc("font", size=10)  # controls default text size
plt.rc("axes", titlesize=10)  # fontsize of the title
plt.rc("axes", labelsize=10)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=10)  # fontsize of the x tick labels
plt.rc("ytick", labelsize=10)  # fontsize of the y tick labels
plt.rc("legend", fontsize=10)  # fontsize of the legend

length = 8 / 2.54  # convert inches to cm
width = 8 / 2.54  # convert inches to cm
fig = plt.figure(figsize=(width, length), tight_layout=True)
ax = plt.subplot(111)
ax.set_title("Different Geometries")
ax.scatter(labels, errors, c=colors, s=10)
ax.set_xlabel(label)
ax.set_yscale("log")
ax.set_ylabel("Error (Ha)")


plt.savefig(
    "/Users/williamsimon/Desktop/Research/QuantumChemistryBenchmarks/figures/geometries_error_vs_{}.pdf".format(
        label
    ),
    dpi=300,
)
plt.close()
