import json
import sys
from helpers import (
    error_running_calculation,
    load_data,
    get_calculation_methods_to_run,
    get_matching_configuration,
    METHOD_MAP,
)
import copy

molecule_types = sys.argv[1]
if molecule_types == "basis":
    from basis_set_molecules import MOLECULES

    data_filename = "data/basis_sets_data.json"
elif molecule_types == "geometry":
    from geometry_molecules import MOLECULES

    data_filename = "data/geometries_data.json"
DATA_DICTIONARY = load_data(data_filename)


for molecule in MOLECULES:
    molecule_configuration = {
        "geometry": molecule.geometry,
        "charge": molecule.charge,
        "multiplicity": molecule.multiplicity,
    }

    (
        preivous_configuration_calculations,
        configuration_index,
    ) = get_matching_configuration(
        DATA_DICTIONARY, molecule.name, molecule_configuration
    )

    molecule_configuration = copy.deepcopy(preivous_configuration_calculations)
    methods_to_run = get_calculation_methods_to_run(preivous_configuration_calculations)

    if len(methods_to_run) > 0:
        print(
            "-------Working on {} (configuration below)-------\n{}".format(
                molecule.name,
                {
                    "geometry": molecule.geometry,
                    "charge": molecule.charge,
                    "multiplicity": molecule.multiplicity,
                },
            ),
            "\n++++ Running the following calculations: ",
            methods_to_run,
            flush=True,
        )

    configuration_updated = False
    for method_name in methods_to_run:
        try:
            molecule_configuration[method_name] = METHOD_MAP[method_name](molecule)

            if "overlap" not in method_name:
                print(
                    method_name,
                    molecule_configuration[method_name]["energy"],
                    flush=True,
                )
            else:

                print(
                    method_name,
                    molecule_configuration[method_name],
                    flush=True,
                )
            configuration_updated = True
        except Exception as e:
            error_running_calculation(method_name, e)
            continue

    if not molecule_configuration.get("number_of_qubits", False):
        try:
            molecule.load()
            if molecule.n_qubits is not None:
                molecule_configuration["number_of_qubits"] = molecule.n_qubits
                configuration_updated = True
        except:
            pass

    if configuration_updated:
        if configuration_index is not None:
            DATA_DICTIONARY[molecule.name][configuration_index] = molecule_configuration
        else:
            configurations_calculated = DATA_DICTIONARY.get(molecule.name, [])
            configurations_calculated.append(molecule_configuration)
            DATA_DICTIONARY[molecule.name] = configurations_calculated

        with open(data_filename, "w") as f:
            f.write(json.dumps(DATA_DICTIONARY))
        f.close()
