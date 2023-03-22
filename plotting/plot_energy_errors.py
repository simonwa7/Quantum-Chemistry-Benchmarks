from turtle import width
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import json
import operator

with open("data/basis_sets_data.json", "r") as f:
    psi4_data = json.loads(f.read())

plt.rc("font", size=10)  # controls default text size
plt.rc("axes", titlesize=10)  # fontsize of the title
plt.rc("axes", labelsize=10)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=10)  # fontsize of the x tick labels
plt.rc("ytick", labelsize=10)  # fontsize of the y tick labels
plt.rc("legend", fontsize=10)  # fontsize of the legend

molecule_names = psi4_data.keys()
number_of_molecules = 0
for molecule_name in molecule_names:
    number_of_molecules += len(psi4_data[molecule_name])
number_of_cols = 4
number_of_rows = int(number_of_molecules / number_of_cols) + 1
fig, axes = plt.subplots(
    number_of_rows,
    number_of_cols,
    figsize=(4 * number_of_cols, 4 * int(number_of_molecules / number_of_cols)),
)

molecule_index = 0
for molecule_name in molecule_names:
    for molecule in psi4_data[molecule_name]:
        row = int(molecule_index / number_of_cols)
        col = molecule_index % number_of_cols
        ax = axes[row][col]

        energies = [
            molecule[calculation_type]["energy"]
            for calculation_type in ["scf", "mp2", "cisd", "ccsd", "fci"]
        ]
        calculation_times = [
            molecule[calculation_type]["cpu_time"]
            for calculation_type in ["scf", "mp2", "cisd", "ccsd", "fci"]
        ]
        fci_energy = molecule["fci"]["energy"]
        energy_errors = [energy - fci_energy for energy in energies]

        scatter = ax.scatter(
            calculation_times[:-1],
            energy_errors[:-1],
            s=5,
            c=["blue", "purple", "red", "green"],
        )
        scatter = ax.scatter(
            [calculation_times[-1]],
            [energy_errors[-1]],
            s=20,
            marker="*",
            c=["orange"],
        )

        ax.set_xlim(0.03, 0.08)
        ax.set_ylim(-0.01, 0.06)
        ax.axhline(y=0, color="black", ls="dashed", linewidth=0.25)
        ax.set_title(molecule_name)
        ax.set_xlabel("CPU Time (s)")
        ax.set_ylabel("Energy Error")

        molecule_index += 1
fig.subplots_adjust(wspace=0.35)
fig.subplots_adjust(hspace=0.35)
plt.savefig("energy_errors.pdf", dpi=600)
