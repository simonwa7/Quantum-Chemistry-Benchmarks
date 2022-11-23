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
            ["Li", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 1.595]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # Geometry from https://github.com/wmkirby1/electronic-structure-hamiltonians
    MolecularData(
        geometry=[
            ["Be", [0.0, 0.0, 0.0]],
            ["H", [0.0, 0.0, 1.3264]],
            ["H", [0.0, 0.0, -1.3264]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # Geometry from https://github.com/wmkirby1/electronic-structure-hamiltonians
    MolecularData(
        geometry=[
            ["O", [0.0, 0.0, 0.1173]],
            ["H", [0.0, -0.7572, -0.4692]],
            ["H", [0.0, 0.7572, -0.4692]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # Geometry from Orca (RHF w/sto-3g)
    MolecularData(  # C8H10
        geometry=[
            ["C", [-7.62102789367626, 1.90439534367021, 0.00239627750678]],
            ["C", [-6.45526027837869, 2.51006484931513, -0.04650982179202]],
            ["H", [-8.55301496888113, 2.45041727944136, -0.04434310942223]],
            ["H", [-7.70527736195038, 0.82975398519597, 0.09180008987937]],
            ["C", [-5.14917557676997, 1.80778043417840, 0.01373803030119]],
            ["H", [-6.40616002837190, 3.58966401651142, -0.13637458471135]],
            ["C", [-3.97753781222587, 2.42106112914756, -0.03579066324710]],
            ["H", [-5.19246888259995, 0.72826456268656, 0.10366086006733]],
            ["C", [-2.67420714310233, 1.72265062785860, 0.02412982193919]],
            ["H", [-3.93625252477051, 3.50072688580607, -0.12570087425851]],
            ["C", [-1.50257002256318, 2.33592465295771, -0.02547997498917]],
            ["H", [-2.71549465366778, 0.64298854784002, 0.11408345352023]],
            ["C", [-0.19648453101413, 1.63364269653481, 0.03475821094021]],
            ["H", [-1.45927943124096, 3.41543935941707, -0.11541850417173]],
            ["C", [0.96927930605355, 2.23930968056795, -0.01420969652286]],
            ["H", [-0.24558177266466, 0.55404800410665, 0.12467786393743]],
            ["H", [1.05352522546160, 3.31394785732737, -0.10365522055868]],
            ["H", [1.90126835036268, 1.69329008743704, 0.03251784158192]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # Geometry from Orca (RHF w/sto-3g)
    MolecularData(  # Formaldehyde
        geometry=[
            ["O", [-1.00344569602166, 3.13257595412551, 0.00000028754081]],
            ["C", [-1.01771485331032, 1.91594716086245, -0.00000114585244]],
            ["H", [-0.10161582392863, 1.30955223695017, -0.07799220640276]],
            ["H", [-1.94778362673938, 1.33120464806187, 0.07799306471439]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # Geometry from Orca (RHF w/sto-3g)
    MolecularData(  # Carbon Dioxide
        geometry=[
            ["C", [-0.18060284717851, 1.29674666446686, 0.00000001319748]],
            ["O", [0.74921337743994, 2.03607153691329, -0.00000000652501]],
            ["O", [-1.11083053026144, 0.55792179861985, -0.00000000667247]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # Geometry from https://pubchem.ncbi.nlm.nih.gov/compound/chrysene#section=2D-Structure
    MolecularData(  # C18H12
        geometry=[
            ["C", [-0.43490, 0.56470, 0.00040]],
            ["C", [0.43500, -0.56470, 0.00040]],
            ["C", [-1.86930, 0.39030, 0.00030]],
            ["C", [1.86940, -0.39030, 0.00020]],
            ["C", [-2.40740, -0.91890, 0.00020]],
            ["C", [2.40740, 0.91880, 0.00010]],
            ["C", [0.16790, 1.83900, 0.00050]],
            ["C", [-0.16790, -1.83910, 0.00040]],
            ["C", [1.55000, 2.01420, 0.00030]],
            ["C", [-1.55000, -2.01410, 0.00030]],
            ["C", [-2.81130, 1.45320, 0.00000]],
            ["C", [2.81130, -1.45320, 0.00000]],
            ["C", [-3.79740, -1.13130, -0.00030]],
            ["C", [3.79730, 1.13130, -0.00030]],
            ["C", [-4.19210, 1.23260, -0.00060]],
            ["C", [4.19210, -1.23250, -0.00040]],
            ["C", [-4.68560, -0.06170, -0.00070]],
            ["C", [4.68560, 0.06160, -0.00070]],
            ["H", [-0.42840, 2.74770, 0.00060]],
            ["H", [0.42840, -2.74780, 0.00040]],
            ["H", [1.94280, 3.02940, 0.00030]],
            ["H", [-1.94280, -3.02940, 0.00020]],
            ["H", [-2.48920, 2.49120, 0.00000]],
            ["H", [2.48920, -2.49120, 0.00010]],
            ["H", [-4.20270, -2.14180, -0.00040]],
            ["H", [4.20260, 2.14170, -0.00040]],
            ["H", [-4.87550, 2.07680, -0.00090]],
            ["H", [4.87550, -2.07670, -0.00070]],
            ["H", [-5.75640, -0.24010, -0.00110]],
            ["H", [5.75640, 0.24010, -0.00110]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # Geometry from https://cccbdb.nist.gov/diatomicexpbondx.asp
    MolecularData(  # C2
        geometry=[
            ["C", [0, 0, 0]],
            ["C", [0, 0, 1.243]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # Geometry from https://pubs.acs.org/doi/pdf/10.1021/jacs.2c06357
    MolecularData(  # Cr2
        geometry=[
            ["Cr", [0, 0, 0]],
            ["Cr", [0, 0, 1.68]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
    # Geometry from https://cccbdb.nist.gov/diatomicexpbondx.asp
    MolecularData(  # BN
        geometry=[
            ["B", [0, 0, 0]],
            ["N", [0, 0, 1.325]],
        ],
        basis="sto-3g",
        multiplicity=1,
    ),
]

BASIS_SETS = [
    "sto-3g",
    "3-21g",
    "6-31g",
    "6-31+g",
    "6-31++g",
    "6-31g*",
    "6-31+g*",
    "6-31++g*",
    "6-311g",
    "6-311+g",
    "6-311++g",
    "6-311g*",
    "6-311+g*",
    "6-311++g*",
    "6-311g**",
    "6-311+g**",
    "6-311++g**",
    "aug-cc-pVXZ",
    "heavy-aug-cc-pVXZ",
    "jun-cc-pVXZ",
    "may-cc-pVXZ",
    "cc-pVXZ",
    "cc-pV(X+d)Z",
    "cc-pCVXZ",
    "cc-pCV(X+d)Z",
    "cc-pwCVXZ",
    "cc-pwCV(X+d)Z",
    "def2-SV(P)",
    "def2-SVP",
    "def2-SVPD",
    "def2-TZVP",
    "def2-TZVPD",
    "def2-TZVPP",
    "def2-TZVPPD",
    "def2-QZVP",
    "def2-QZVPD",
    "def2-QZVPP",
    "def2-QZVPPD",
]
ALL_MOLECULES = []
print("beginning loop")
print(len(MOLECULES))
for molecule in MOLECULES:
    print(molecule)
    for basis in BASIS_SETS:
        print(basis)
        ALL_MOLECULES.append(
            MolecularData(
                geometry=molecule.geometry,
                basis=basis,
                multiplicity=molecule.multiplicity,
            )
        )
MOLECULES = ALL_MOLECULES
