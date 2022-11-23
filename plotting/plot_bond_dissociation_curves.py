import matplotlib.pyplot as plt
import json

molecule_name = "H2_sto-3g_singlet"
# molecule_name = "H1-F1_sto-3g_singlet"

with open("data/cluster_psi4_statistics.json", "r") as f:
    molecule_data = json.loads(f.read())[molecule_name]

bond_lengths = [
    configuration["geometry"][1][1][2] for configuration in molecule_data[1:]
]
scf_energies = [configuration["scf"]["energy"] for configuration in molecule_data[1:]]
mp2_energies = [configuration["mp2"]["energy"] for configuration in molecule_data[1:]]
cisd_energies = [configuration["cisd"]["energy"] for configuration in molecule_data[1:]]
ccsd_energies = [configuration["ccsd"]["energy"] for configuration in molecule_data[1:]]
fci_energies = [configuration["fci"]["energy"] for configuration in molecule_data[1:]]
number_of_configurations = len(bond_lengths)

plt.rc("font", size=10)  # controls default text size
plt.rc("axes", titlesize=10)  # fontsize of the title
plt.rc("axes", labelsize=10)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=10)  # fontsize of the x tick labels
plt.rc("ytick", labelsize=10)  # fontsize of the y tick labels
plt.rc("legend", fontsize=10)  # fontsize of the legend

start_index = 35

fig, axes = plt.subplots(
    2,
    1,
    figsize=(8, 8),
)


ax = axes[0]
ax.set_xlabel("Bond Length")
ax.set_ylabel("Energy")
ax.set_title(molecule_name)
ax.plot(
    bond_lengths[start_index:],
    scf_energies[start_index:],
    label="SCF",
    color="blue",
    lw=2,
)
ax.plot(
    bond_lengths[start_index:],
    mp2_energies[start_index:],
    label="MP2",
    color="orange",
    lw=2,
)
ax.plot(
    bond_lengths[start_index:],
    cisd_energies[start_index:],
    label="CISD",
    color="purple",
    lw=2,
)
ax.plot(
    bond_lengths[start_index:],
    ccsd_energies[start_index:],
    label="CCSD",
    color="green",
    lw=2,
)
ax.plot(
    bond_lengths[start_index:],
    fci_energies[start_index:],
    label="FCI",
    color="red",
    lw=2,
    ls="dashed",
)
ax.legend()


ax = axes[1]
ax.set_xlabel("Bond Length")
ax.set_ylabel("Energy Error from FCI")
ax.set_yscale("log", base=10)
scf_energy_errors = [
    scf_energies[i] - fci_energy for i, fci_energy in enumerate(fci_energies)
]
mp2_energy_errors = [
    mp2_energies[i] - fci_energy for i, fci_energy in enumerate(fci_energies)
]
cisd_energy_errors = [
    cisd_energies[i] - fci_energy for i, fci_energy in enumerate(fci_energies)
]
ccsd_energy_errors = [
    ccsd_energies[i] - fci_energy for i, fci_energy in enumerate(fci_energies)
]
ax.plot(
    bond_lengths[start_index:],
    scf_energy_errors[start_index:],
    label="SCF",
    color="blue",
    lw=2,
)
ax.plot(
    bond_lengths[start_index:],
    mp2_energy_errors[start_index:],
    label="MP2",
    color="orange",
    lw=2,
)
ax.plot(
    bond_lengths[start_index:],
    cisd_energy_errors[start_index:],
    label="CISD",
    color="purple",
    lw=2,
)
ax.plot(
    bond_lengths[start_index:],
    ccsd_energy_errors[start_index:],
    label="CCSD",
    color="green",
    lw=2,
)

plt.show()
