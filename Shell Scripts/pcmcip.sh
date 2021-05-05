#!/bin/tcsh
#SBATCH -t 96:00:00
#SBATCH -n 8
#SBATCH --mem-per-cpu=2048
#SBATCH --share


. ~/.profile

echo "Starting pcmci parcorr"
python3 tigramite/pcmci_parcorr.py > pcmci_parcorr.txt
echo "pcmci parcorr Finished"