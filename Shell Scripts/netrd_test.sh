#!/bin/tcsh
#SBATCH -t 1
#SBATCH -n 4
#SBATCH --mem-per-cpu=128
#SBATCH --share

. ~/.profile

echo "Starting correlation matrix"
python3  mean_field.py > shrek.txt
echo "Correlation matrix finished"