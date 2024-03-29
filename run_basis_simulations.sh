#!/bin/bash
#SBATCH -J qchem-basis-simulations
#SBATCH -p batch 
#SBATCH --time=7-00:00:00
#SBATCH -n 1
#SBATCH -c 8
#SBATCH --mem=100000
module load anaconda/3
source activate /cluster/tufts/lovelab/wsimon02/condaenv/qchem
python3 run_calculations.py basis