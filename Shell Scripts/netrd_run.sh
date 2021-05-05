#!/bin/tcsh
#SBATCH -t 24:00:00
#SBATCH -n 8
#SBATCH --mem-per-cpu=2048
#SBATCH --share

. ~/.profile

echo "Starting correlation matrix"
python3 correlation_matrix.py > corr_matrix.txt
echo "Correlation matrix finished"

echo "Starting correlation spanning tree"
python3 correlation_spanning_tree.py > corr_span_tree.txt
echo "Correlation spanning tree finished"

echo "Starting free energy min"
python3 free_energy_min.py > free_energy_min.txt
echo "Free energy min finished"

echo "Starting Granger Causality"
python3 granger_causality.py > granger.txt
echo "Granger Causality finished"

echo "Starting Graphical Lasso"
python3 graphical_lasso.py > graphical_lasso.txt
echo "Graphical Lasso finished"

echo "Starting marchenko pastur"
python3 marchenko_pastur.py > marchenko.txt
echo "Marchenko pastur complete"

echo "Starting max likelihood"
python3 max_likelihood.py > max_likelihood.txt
echo "Max likelihood complete"

echo "Starting Mean Field"
python3 mean_field.py > mean_field.txt
echo "Mean field finished"

echo "Starting mutual info"
python3 mutual_info.py > mutual_info.txt
echo "Mutual info finished"

echo "Starting naive transfer entropy"
python3 naive_transfer_entropy.py > naive_transfer_entropy.txt
echo "Naive transfer entropy finished"

echo "Starting optimal causal entropy"
python3 optimal_causal_entropy.py > optimal_causal_entropy.txt 
echo "optimal causal entropy finished"

echo "Starting ou inference entropy"
python3 ou_inference.py > ou_inference.txt
echo "ou inference finished"

echo "Starting partial correlation influence"
python3 partial_corr_influence.py > partial_corr_influence.txt
echo "Partial correlation influence done"

echo "Starting partial correlation matrix"
python3 partial_corr_matrix.py > partial_corr_matrix.txt
echo "Partial correlation matrix finished"

echo "Starting random reconstructor"
python3 random_reconstructor.py > random_reconstructor.txt
echo "random reconstructor finished"

echo "Starting thouless anderson"
python3 thouless_anderson.py > thouless_anderson.txt
echo "thouless anderson finished"

