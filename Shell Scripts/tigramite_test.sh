#!/bin/tcsh
#SBATCH -t 10
#SBATCH -n 8
#SBATCH --mem-per-cpu=2048
#SBATCH --share

. ~/.profile

echo "Starting FullCi gpdc"
python3 fullci_gpdc.py > fullci_gpdc.txt
echo "FullCi gpdc Finished"