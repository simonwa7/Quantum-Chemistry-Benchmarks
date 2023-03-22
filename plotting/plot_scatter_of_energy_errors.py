from utils import plot_method_errors_against_eachother

methods = [
    "scf",
    "mp2",
    "cisd",
    "ccsd",
    "nc_SingleSweep_magnitude",
    # "nc_DFS_magnitude",
    # "nc_DFS_largest",
    # "nc_SingleSweep_CurrentOrder",
    # "nc_SingleSweep_random",
    # "nc_diag",
    # "nc_basis",
]

data_dir = "/Users/williamsimon/Desktop/Research/QuantumChemistryBenchmarks/data/"

from itertools import combinations

for method1, method2 in combinations(methods, 2):
    plot_method_errors_against_eachother(
        data_dir + "geometries" + "_data.json", method1, method2
    )
