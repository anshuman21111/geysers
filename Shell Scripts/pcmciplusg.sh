#!/bin/tcsh
#SBATCH -t 96:00:00
#SBATCH -n 8
#SBATCH --mem-per-cpu=2048
#SBATCH --share


. ~/.profile

echo "Starting pcmciplus gpdc"
python3 tigramite/pcmciplus_gpdc.py > pcmciplus_gpdc.txt
echo "pcmci pcmciplus gpdc Finished"