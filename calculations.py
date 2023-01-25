from time import process_time
from openfermionpsi4 import run_psi4
from functools import partial
from symmer.symplectic import PauliwordOp
from symmer.utils import exact_gs_energy
from symmer.projection import QubitTapering
from symmer.projection import ContextualSubspace
import numpy as np
from openfermion.transforms import get_fermion_operator, jordan_wigner
from openfermionpsi4 import run_psi4


def run_fci(molecule):
    start = process_time()
    fci_molecule = run_psi4(
        molecule,
        run_fci=1,
        verbose=False,
    )
    cpu_time = process_time() - start
    return {
        "energy": fci_molecule.fci_energy.tolist(),
        "orbital_energies": list(fci_molecule.orbital_energies),
        "cpu_time": cpu_time,
        # "memory": memory_usage,
    }


def run_hf(molecule):
    start = process_time()
    scf_molecule = run_psi4(
        molecule,
        run_scf=1,
        verbose=False,
    )
    cpu_time = process_time() - start
    return {
        "energy": scf_molecule.hf_energy.tolist(),
        "orbital_energies": list(scf_molecule.orbital_energies),
        "cpu_time": cpu_time,
        # "memory": memory_usage,
    }


def run_mp2(molecule):
    start = process_time()
    mp2_molecule = run_psi4(
        molecule,
        run_mp2=1,
        verbose=False,
    )
    cpu_time = process_time() - start
    return {
        "energy": mp2_molecule.mp2_energy.tolist(),
        "orbital_energies": list(mp2_molecule.orbital_energies),
        "cpu_time": cpu_time,
        # "memory": memory_usage,
    }


def run_cisd(molecule):
    start = process_time()
    cisd_molecule = run_psi4(
        molecule,
        run_cisd=1,
        verbose=False,
    )
    cpu_time = process_time() - start
    return {
        "energy": cisd_molecule.cisd_energy.tolist(),
        "orbital_energies": list(cisd_molecule.orbital_energies),
        "cpu_time": cpu_time,
        # "memory": memory_usage,
    }


def run_ccsd(molecule):
    start = process_time()
    ccsd_molecule = run_psi4(
        molecule,
        run_ccsd=1,
        verbose=False,
    )
    cpu_time = process_time() - start
    return {
        "energy": ccsd_molecule.ccsd_energy.tolist(),
        "orbital_energies": list(ccsd_molecule.orbital_energies),
        "cpu_time": cpu_time,
        # "memory": memory_usage,
    }


def _get_qubit_hamiltonian_from_molecule(molecule):
    try:
        molecule.load()
    except:
        molecule = run_psi4(
            molecule,
            run_scf=1,
            run_mp2=1,
            run_ccsd=1,
            run_cisd=1,
            run_fci=1,
            verbose=False,
        )
        molecule.save()
        molecule.load()
    # Get the Hamiltonian in an active space.
    molecular_hamiltonian = molecule.get_molecular_hamiltonian()

    # Map operator to fermions and qubits.
    fermion_hamiltonian = get_fermion_operator(molecular_hamiltonian)
    qubit_hamiltonian = jordan_wigner(fermion_hamiltonian)
    qubit_hamiltonian.compress()
    return qubit_hamiltonian


def run_nc(molecule, strategy="SingleSweep_magnitude"):
    """TODO: Not Yet Ready"""
    start = process_time()
    nc_data = {}
    # 1. Generate Molecular Hamiltonian
    qubit_hamiltonian = _get_qubit_hamiltonian_from_molecule(molecule)

    # 2. Import to Symmer
    hamiltonian = PauliwordOp.from_openfermion(qubit_hamiltonian)

    # 3. Calculate Reference Energy
    gs_energy, _ = exact_gs_energy(hamiltonian.to_sparse_matrix)
    nc_data["full-diagonalized_energy"] = gs_energy

    # 4. Tapering
    hartree_fock_array = np.hstack(
        (
            np.ones(molecule.n_electrons),
            np.zeros(molecule.n_qubits - molecule.n_electrons),
        )
    )
    hartree_fock_array = np.array(hartree_fock_array, dtype=int)
    tapered_hamiltonian = QubitTapering(hamiltonian).taper_it(
        ref_state=hartree_fock_array
    )

    # 5. Calculate Energy Error from Tapering
    tapered_gs_energy, _ = exact_gs_energy(tapered_hamiltonian.to_sparse_matrix)
    nc_data["tapered-diagonalized_energy"] = tapered_gs_energy

    # 6. Calculate NC Approximation
    try:
        cs_vqe = ContextualSubspace(
            tapered_hamiltonian, noncontextual_strategy=strategy
        )
        nc_data["energy"] = cs_vqe.noncontextual_operator.energy
        nc_data["cpu_time"] = process_time() - start
        return nc_data
    except RuntimeError as e:
        raise AttributeError(e.__str__)


METHOD_MAP = {
    # "scf": run_hf,
    # "mp2": run_mp2,
    # "cisd": run_cisd,
    # "ccsd": run_ccsd,
    # "fci": run_fci,
    # "nc_SingleSweep_magnitude": partial(run_nc, strategy="SingleSweep_magnitude"),
    # "nc_DFS_magnitude": partial(run_nc, strategy="DFS_magnitude"),
    # "nc_DFS_largest": partial(run_nc, strategy="DFS_largest"),
    # "nc_SingleSweep_CurrentOrder": partial(run_nc, strategy="SingleSweep_CurrentOrder"),
    # "nc_SingleSweep_random": partial(run_nc, strategy="SingleSweep_random"),
    # "nc_diag": partial(run_nc, strategy="diag"),
    # "nc_basis": partial(run_nc, strategy="basis"),
}
