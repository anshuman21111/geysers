#!/bin/tcsh
#SBATCH -t 96:00:00
#SBATCH -n 8
#SBATCH --mem-per-cpu=2048
#SBATCH --share


. ~/.profile

echo "Starting pcmci gpdc"
python3 tigramite/pcmci_gpdc.py > pcmci_gpdc.txt
echo "pcmci gpdc Finished"