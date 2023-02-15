import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import numpy as np


def get_method_errors_and_labels(data, method, label):
    method_energies = []
    molecule_names = []
    labels = []
    fci_energies = {}

    for molecule_name, molecule_data in data.items():
        name = molecule_name[: molecule_name.find("_")]

        if not fci_energies.get(name, False):
            fci_energies[name] = 1e10

        for configuration in molecule_data:
            if (
                configuration.get("fci", False)
                and configuration.get(method, False)
                and configuration.get(label, False)
            ):
                molecule_names.append(name)
                fci_energies[name] = min(
                    fci_energies[name], configuration["fci"]["energy"]
                )
                method_energies.append(configuration[method]["energy"])
                labels.append(configuration[label])

    return [
        abs(method_energy - fci_energies[molecule_name])
        for molecule_name, method_energy in zip(molecule_names, method_energies)
    ], labels


def plot_method_errors_against_eachother(data_filename, methodx, methody, legend=False):

    np.random.seed(2)

    type = "Geometries"
    if "basis_sets" in data_filename:
        type = "Basis Sets"

    with open(data_filename, "r") as f:
        data = json.loads(f.read())

    methodx_energies = []
    methody_energies = []
    fci_energies = {}
    molecule_names = []
    color_map = {}
    all_colors = list(mcolors.CSS4_COLORS.keys())
    colors = []

    for molecule_name, molecule_data in data.items():
        name = molecule_name[: molecule_name.find("_")]
        if not fci_energies.get(name, False):
            fci_energies[name] = 1e10
        if not color_map.get(name, False):
            color = np.random.choice(all_colors)
            color_map[name] = color
            all_colors.remove(color)
        for configuration in molecule_data:
            if (
                configuration.get("fci", False)
                and configuration.get(methodx, False)
                and configuration.get(methody, False)
            ):
                fci_energies[name] = min(
                    fci_energies[name], configuration["fci"]["energy"]
                )
                molecule_names.append(name)
                colors.append(color_map[name])
                methodx_energies.append(configuration[methodx]["energy"])
                methody_energies.append(configuration[methody]["energy"])

    methodx_errors = [
        abs(methodx_energy - fci_energies[molecule_name])
        for molecule_name, methodx_energy in zip(molecule_names, methodx_energies)
    ]
    methody_errors = [
        abs(methody_energy - fci_energies[molecule_name])
        for molecule_name, methody_energy in zip(molecule_names, methody_energies)
    ]

    plt.rc("font", size=10)  # controls default text size
    plt.rc("axes", titlesize=10)  # fontsize of the title
    plt.rc("axes", labelsize=10)  # fontsize of the x and y labels
    plt.rc("xtick", labelsize=10)  # fontsize of the x tick labels
    plt.rc("ytick", labelsize=10)  # fontsize of the y tick labels
    plt.rc("legend", fontsize=10)  # fontsize of the legend

    length = 6 / 2.54  # convert inches to cm
    width = 8 / 2.54  # convert inches to cm
    if legend:
        length = 10 / 2.54
    fig = plt.figure(figsize=(width, length), tight_layout=True)
    ax = plt.subplot(111)
    ax.set_title("{}: Error of {} vs {}".format(type, methodx, methody))
    ax.scatter(methodx_errors, methody_errors, c=colors, s=10)
    ax.set_xlabel("$\Delta_{}$ (Ha)".format("{" + methodx.replace("_", "\_") + "}"))
    ax.set_ylabel("$\Delta_{}$ (Ha)".format("{" + methody.replace("_", "\_") + "}"))

    if legend:

        from matplotlib.lines import Line2D

        legend_elements = [
            Line2D(
                [0],
                [0],
                marker="o",
                color=color,
                label=molecule_name,
            )
            for molecule_name, color in color_map.items()
        ]

        # Shrink current axis
        box = ax.get_position()
        # ax.set_position([box.x0, box.y0, box.width * (0.775 * 3 / 2), box.height])
        ax.set_position(
            [box.x0, box.y0 + (box.height * (1 / 6)), box.width, box.height * (5 / 6)]
        )

        # Put a legend below current axis
        plt.legend(
            handles=legend_elements,
            loc="upper center",
            bbox_to_anchor=(0.5, -1),
            ncol=4,
            prop={"size": 5},
        )

    plt.savefig(
        "/Users/williamsimon/Desktop/Research/QuantumChemistryBenchmarks/figures/error_plots/{}:{}_vs_{}.pdf".format(
            type, methodx, methody
        ),
        dpi=300,
    )
    plt.close()
