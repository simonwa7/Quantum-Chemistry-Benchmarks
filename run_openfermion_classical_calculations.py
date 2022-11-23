from openfermionpsi4 import run_psi4
from time import process_time
import json
import os
import sys


def check_if_configuration_has_been_calculated(data, molecule_name, configuration):
    # This checks the data in psi4_statistics.json to see if the current configuration has already been calculated
    configuration_already_calculated = False
    configurations_calculated = data.get(molecule_name, [])
    if len(configurations_calculated) != 0:
        for previous_configuration in data[molecule_name]:
            matching_configuration = True
            for key in configuration.keys():
                if configuration[key] != previous_configuration[key]:
                    matching_configuration = False

            if matching_configuration:
                configuration_already_calculated = True

    return configuration_already_calculated


def error_running_calculation(molecule_configuration):
    print(
        "Error calculating CISD for current configuration:\n",
        molecule_configuration,
    )
    print("Skipping geometry")


molecule_types = sys.argv[1]
if molecule_types == "basis":
    from basis_set_molecules import MOLECULES

    data_filename = "data/basis_sets_data.json"
elif molecule_types == "geometry":
    from geometry_molecules import MOLECULES

    data_filename = "data/geometries_data.json"
# Data is formatted as:
# molecule name: [
# {
#   "geometry": xxx,
# "charge": x,
# "multiplicity": x,
# "<method>": {
# "energy": x,
# "cpu_time": x
# "<additional kwargs>": x,
# }
# }
# ]
DATA_DICTIONARY = {}
if os.path.exists(data_filename):
    with open(data_filename, "r") as f:
        DATA_DICTIONARY = json.loads(f.read())

for molecule in MOLECULES:
    molecule_configuration = {
        "geometry": molecule.geometry,
        "charge": molecule.charge,
        "multiplicity": molecule.multiplicity,
    }
    print(
        "-------Working on {} (configuration below)-------\n{}".format(
            molecule.name, molecule_configuration
        )
    )

    if not check_if_configuration_has_been_calculated(
        DATA_DICTIONARY, molecule.name, molecule_configuration
    ):

        # Run HF SCF Calcs
        try:
            start = process_time()
            scf_molecule = run_psi4(
                molecule,
                run_scf=1,
                verbose=False,
            )
            cpu_time = process_time() - start
            molecule_configuration["scf"] = {
                "energy": scf_molecule.hf_energy.tolist(),
                "orbital_energies": list(scf_molecule.orbital_energies),
                "cpu_time": cpu_time,
                # "memory": memory_usage,
            }
            print("SCF ", scf_molecule.hf_energy.tolist())
        except AttributeError as e:
            error_running_calculation(molecule_configuration)
            continue

        # Run MP2 Calcs
        try:
            start = process_time()
            mp2_molecule = run_psi4(
                molecule,
                run_mp2=1,
                verbose=False,
            )
            cpu_time = process_time() - start
            molecule_configuration["mp2"] = {
                "energy": mp2_molecule.mp2_energy.tolist(),
                "orbital_energies": list(mp2_molecule.orbital_energies),
                "cpu_time": cpu_time,
                # "memory": memory_usage,
            }
            print("MP2 ", mp2_molecule.mp2_energy.tolist())
        except AttributeError as e:
            error_running_calculation(molecule_configuration)
            continue

        # Run CISD Calcs
        try:
            start = process_time()
            cisd_molecule = run_psi4(
                molecule,
                run_cisd=1,
                verbose=False,
            )
            cpu_time = process_time() - start
            molecule_configuration["cisd"] = {
                "energy": cisd_molecule.cisd_energy.tolist(),
                "orbital_energies": list(cisd_molecule.orbital_energies),
                "cpu_time": cpu_time,
                # "memory": memory_usage,
            }
            print("CISD ", cisd_molecule.cisd_energy.tolist())
        except AttributeError as e:
            error_running_calculation(molecule_configuration)
            continue

        # Run CCSD Calcs
        try:
            start = process_time()
            ccsd_molecule = run_psi4(
                molecule,
                run_ccsd=1,
                verbose=False,
            )
            cpu_time = process_time() - start
            molecule_configuration["ccsd"] = {
                "energy": ccsd_molecule.ccsd_energy.tolist(),
                "orbital_energies": list(ccsd_molecule.orbital_energies),
                "cpu_time": cpu_time,
                # "memory": memory_usage,
            }
            print("CCSD ", ccsd_molecule.ccsd_energy.tolist())
        except AttributeError as e:
            error_running_calculation(molecule_configuration)
            continue

        # Run FCI Calcs
        try:
            start = process_time()
            fci_molecule = run_psi4(
                molecule,
                run_fci=1,
                verbose=False,
            )
            cpu_time = process_time() - start
            molecule_configuration["fci"] = {
                "energy": fci_molecule.fci_energy.tolist(),
                "orbital_energies": list(fci_molecule.orbital_energies),
                "cpu_time": cpu_time,
                # "memory": memory_usage,
            }
            print("FCI ", fci_molecule.fci_energy.tolist())
        except AttributeError as e:
            error_running_calculation(molecule_configuration)
            continue

        configurations_calculated = DATA_DICTIONARY.get(molecule.name, [])
        configurations_calculated.append(molecule_configuration)
        DATA_DICTIONARY[molecule.name] = configurations_calculated

        with open(data_filename, "w") as f:
            f.write(json.dumps(DATA_DICTIONARY))
        f.close()
