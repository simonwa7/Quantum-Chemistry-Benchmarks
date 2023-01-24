import os
import json
from calculations import METHOD_MAP


def get_matching_configuration(data, molecule_name, configuration):
    # Find entry with matching geometry, charge, and multiplicity
    configurations_calculated = data.get(molecule_name, [])
    if len(configurations_calculated) != 0:
        for index, previous_configuration in enumerate(data[molecule_name]):
            matching_configuration = True
            for key in configuration.keys():
                if configuration[key] != previous_configuration[key]:
                    matching_configuration = False

            if matching_configuration:
                return previous_configuration, index
    return configuration, None


def get_calculation_methods_to_run(previous_results):
    methods_to_calculate = []
    for method in METHOD_MAP.keys():
        if method not in previous_results:
            methods_to_calculate.append(method)
    return methods_to_calculate


def error_running_calculation(method_name, error_message):
    print(
        "Error calculating {} for current configuration:\n".format(method_name),
        error_message,
    )


def load_data(data_filename):
    # Data is formatted as:
    # "molecule name": [
    #   {
    #     "geometry": xxx,
    #     "charge": x,
    #     "multiplicity": x,
    #     "<method>": {
    #       "energy": x,
    #       "cpu_time": x
    #       "<additional kwargs>": x,
    #     }
    #   }
    # ]
    data = {}
    if os.path.exists(data_filename):
        with open(data_filename, "r") as f:
            data = json.loads(f.read())
    return data


def check_if_configuration_has_been_calculated(data, molecule_name, configuration):
    # This checks the data to see if the current configuration has already been calculated
    previous_results, _ = get_matching_configuration(data, molecule_name, configuration)
    if previous_results == configuration:
        return False
    return True
