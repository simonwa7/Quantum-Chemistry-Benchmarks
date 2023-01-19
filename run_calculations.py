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

    print(
        "-------Working on {} (configuration below)-------\n{}".format(
            molecule.name, molecule_configuration
        ),
    )

    preivous_configuration_calculations = get_matching_configuration(
        DATA_DICTIONARY, molecule.name, molecule_configuration
    )

    molecule_configuration = copy.deepcopy(preivous_configuration_calculations)
    methods_to_run = get_calculation_methods_to_run(preivous_configuration_calculations)
    for method_name in methods_to_run:
        try:
            molecule_configuration[method_name] = METHOD_MAP[method_name](molecule)
            print(method_name, molecule_configuration[method_name]["energy"])
        except AttributeError as e:
            error_running_calculation(method_name, e)
            continue

    if molecule_configuration != preivous_configuration_calculations:
        configurations_calculated = DATA_DICTIONARY.get(molecule.name, [])
        configurations_calculated.append(molecule_configuration)
        DATA_DICTIONARY[molecule.name] = configurations_calculated

        with open(data_filename, "w") as f:
            f.write(json.dumps(DATA_DICTIONARY))
        f.close()
