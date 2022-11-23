from openfermion.chem import MolecularData
import numpy as np

MOLECULES = [
    MolecularData(
        geometry=[
            ["H", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 0.7414]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    MolecularData(
        geometry=[
            ["H", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 0.7414]],
        ],
        basis="3-21g",
        multiplicity=1,
    ),
    MolecularData(
        geometry=[
            ["H", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 0.7414]],
        ],
        basis="6-31g",
        multiplicity=1,
    ),
    MolecularData(
        geometry=[
            ["He", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 0.772]],
        ],
        basis="sto-3g",
        multiplicity=1,
        charge=1,
    ),
    MolecularData(
        geometry=[
            ["He", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 0.772]],
        ],
        basis="3-21g",
        multiplicity=1,
        charge=1,
    ),
    MolecularData(
        geometry=[
            ["He", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 0.772]],
        ],
        basis="6-31g",
        multiplicity=1,
        charge=1,
    ),
    MolecularData(
        geometry=[
            ["H", [0.0, 0.0, 0.0]],
            ["F", [0.0, 0.0, 0.9168]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    MolecularData(
        geometry=[
            ["H", [0.0, 0.0, 0.0]],
            ["F", [0.0, 0.0, 0.9168]],
        ],
        basis="3-21g",
        multiplicity=1,
    ),
    MolecularData(
        geometry=[
            ["H", [0.0, 0.0, 0.0]],
            ["H", [0.90, 0.0, 0.0]],
            ["H", [0.45, 0.779422863, 0.0]],
        ],
        basis="sto-3g",
        multiplicity=1,
        charge=1,
    ),
    # Calculated with Orca using charge 1 (TODO: update to neutral charge
    MolecularData(
        geometry=[
            ["H", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 0.83889732965221]],
            ["H", [0.0, 0.0, 1.67779465930442]],
        ],
        basis="sto-3g",
        multiplicity=2,
    ),
    MolecularData(
        geometry=[
            ["Li", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 1.595]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    MolecularData(
        geometry=[
            ["Li", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 1.595]],
        ],
        basis="3-21g",
        multiplicity=1,
    ),
    MolecularData(
        geometry=[
            ["B", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 1.2324]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    MolecularData(
        geometry=[
            ["N", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 1.0362]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # TOD
    MolecularData(
        geometry=[["H", [0.0, 0.0, i * 0.7414]] for i in range(4)],
        basis="sto-3g",
        multiplicity=1,
    ),
    # TOD
    MolecularData(
        geometry=[["H", [0.0, 0.0, i * 0.7414]] for i in range(6)],
        basis="sto-3g",
        multiplicity=1,
    ),
    # TOD
    MolecularData(
        geometry=[["H", [0.0, 0.0, i * 0.7414]] for i in range(8)],
        basis="sto-3g",
        multiplicity=1,
    ),
    # TOD
    MolecularData(
        geometry=[["H", [0.0, 0.0, i * 0.7414]] for i in range(10)],
        basis="sto-3g",
        multiplicity=1,
    ),
    # TOD
    MolecularData(
        geometry=[["H", [0.0, 0.0, i * 0.7414]] for i in range(12)],
        basis="sto-3g",
        multiplicity=1,
    ),
    # TOD
    MolecularData(
        geometry=[
            ["Be", [-1.42719, 0.98858, -0.01035]],
            ["H", [-0.45930, 1.02829, 0.01371]],
            ["H", [-1.70604, 1.78220, 0.47065]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # TOD
    MolecularData(
        geometry=[
            ["C", [0.0, 0.0, 0.1027]],
            ["H", [0.0, 1.0042, -0.3081]],
            ["H", [0.0, -1.0042, -0.3081]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # TOD
    MolecularData(
        geometry=[
            ["Na", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 1.595]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # TOD
    MolecularData(
        geometry=[
            ["K", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 1.595]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    MolecularData(
        geometry=[
            ["O", [-1.42719, 0.98858, -0.01035]],
            ["H", [-0.45930, 1.02829, 0.01371]],
            ["H", [-1.70604, 1.78220, 0.47065]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    MolecularData(
        geometry=[
            ["N", [0.0, 0.0, 0.0]],
            ["H", [0.0, -0.9377, -0.3816]],
            ["H", [0.8121, 0.4689, -0.3816]],
            ["H", [-0.8121, 0.4689, -0.3816]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # MolecularData(
    #     geometry=[
    #         ["C", [0.0, 0.0, 0.0]],
    #         ["H", [0.6276, 0.6276, 0.6276]],
    #         ["H", [0.6276, -0.6276, -0.6276]],
    #         ["H", [-0.6276, 0.6276, -0.6276]],
    #     ],
    #     basis="sto-3g",
    #     multiplicity=1,
    # ),
    MolecularData(
        geometry=[["F", [0.0, 0.0, 0.0]], ["F", [0.0, 0.0, 1.4119]]],
        basis="sto-3g",
        multiplicity=1,
    ),
    MolecularData(
        geometry=[["N", [0.0, 0.0, 0.0]], ["N", [0.0, 0.0, 0.5488]]],
        basis="sto-3g",
        multiplicity=1,
    ),
    MolecularData(
        geometry=[["O", [0.0, 0.0, 0.0]], ["O", [0.0, 0.0, 1.2075]]],
        basis="sto-3g",
        multiplicity=1,
    ),
    MolecularData(
        geometry=[["C", [0.0, 0.0, 0.0]], ["O", [0.0, 0.0, 1.1282]]],
        basis="sto-3g",
        multiplicity=1,
    ),
    MolecularData(
        geometry=[["H", [0.0, 0.0, 0.0]], ["Cl", [0.0, 0.0, 1.2746]]],
        basis="sto-3g",
        multiplicity=1,
    ),
    # TOD
    MolecularData(
        geometry=[
            ["C", [-1.42719, 0.98858, -0.01035]],
            ["O", [-0.45930, 1.02829, 0.01371]],
            ["O", [-1.70604, 1.78220, 0.47065]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # TOD
    MolecularData(
        geometry=[
            ["Rb", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 1.595]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # TOD
    MolecularData(
        geometry=[
            ["S", [0.0, 0.0, 0.103]],
            ["H", [0.0, 0.9616, -0.8239]],
            ["H", [0.0, -0.9616, -0.8239]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # # TOD
    # MolecularData(
    #     geometry=[
    #         ["Li", [0.0, 0.0, -1.5816]],
    #         ["O", [0.0, 0.0, 0.0]],
    #         ["H", [0.0, 0.0, 0.9691]],
    #     ],
    #     basis="3-21g",
    #     multiplicity=1,
    # ),
    MolecularData(
        geometry=[
            ["Mg", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 1.7246]],
            ["H", [0.0, 0.0, -1.7246]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
]

import pdb

DIATOMIC_MOLECULE_SCANS = []
for molecule in MOLECULES:
    if len(molecule.geometry) == 2:
        second_atom = molecule.geometry[1][0]
        DIATOMIC_MOLECULE_SCANS += [
            MolecularData(
                geometry=[
                    molecule.geometry[0],
                    [second_atom, [0.0, 0.0, bond_length]],
                ],
                basis=molecule.basis,
                multiplicity=molecule.multiplicity,
            )
            for bond_length in np.linspace(0, 10, 1000)
        ]

MOLECULES += DIATOMIC_MOLECULE_SCANS
