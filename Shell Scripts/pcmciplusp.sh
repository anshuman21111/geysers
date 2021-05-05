#!/bin/tcsh
#SBATCH -t 96:00:00
#SBATCH -n 8
#SBATCH --mem-per-cpu=2048
#SBATCH --share


. ~/.profile

echo "Starting pcmciplus parcorr"
python3 tigramite/pcmciplus_parcorr.py > pcmciplus_parcorr.txt
echo "pcmci pcmciplus parcorr Finished"