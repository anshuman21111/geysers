#!/bin/tcsh
#SBATCH -t 96:00:00
#SBATCH -n 8
#SBATCH --mem-per-cpu=2048
#SBATCH --share

. ~/.profile

echo "Starting FullCi gpdc"
python3 tigramite/fullci_gpdc.py > fullci_gpdc.txt
echo "FullCi gpdc Finished"

echo "Starting FullCi parcorr"
python3 tigramite/fullci_parcorr.py > fullci_parcorr.txt
echo "FullCi parcorr Finished"

echo "Starting pcmci gpdc"
python3 tigramite/pcmci_gpdc.py > pcmci_gpdc.txt
echo "pcmci gpdc Finished"

echo "Starting pcmci parcorr"
python3 tigramite/pcmci_parcorr.py > pcmci_parcorr.txt
echo "pcmci parcorr Finished"

echo "Starting pcmciplus gpdc"
python3 tigramite/pcmciplus_gpdc.py > pcmciplus_gpdc.txt
echo "pcmci pcmciplus gpdc Finished"

echo "Starting pcmciplus parcorr"
python3 tigramite/pcmciplus_parcorr.py > pcmciplus_parcorr.txt
echo "pcmci pcmciplus parcorr Finished"