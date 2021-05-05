#!/bin/tcsh
#SBATCH -t 48:00:00
#SBATCH -n 8
#SBATCH --mem-per-cpu=2048
#SBATCH --share


. ~/.profile

echo "Starting pcmciplus parcorr"
python3 prediction.py
echo "pcmci pcmciplus parcorr Finished"