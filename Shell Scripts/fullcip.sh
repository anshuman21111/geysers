#!/bin/tcsh
#SBATCH -t 96:00:00
#SBATCH -n 8
#SBATCH --mem-per-cpu=2048
#SBATCH --share


. ~/.profile

echo "Starting FullCi parcorr"
python3 tigramite/fullci_parcorr.py > fullci_parcorr.txt
echo "FullCi parcorr Finished"