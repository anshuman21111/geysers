import numpy as np
import matplotlib
from matplotlib import pyplot as plt

import sklearn

import tigramite
from tigramite import data_processing as pp
from tigramite import plotting as tp
from tigramite.pcmci import PCMCI
from tigramite.independence_tests import ParCorr, GPDC, CMIknn, CMIsymb

import pandas as pd

df = pd.read_csv('collation.csv')
df.drop(df.columns[[0]], axis = 1, inplace = True)
df.drop(df.columns[[0]], axis = 1, inplace = True)
df.drop(columns = ['AU', 'LC', 'RI'], inplace = True)
var_names = df.columns
df = df.dropna()
df = df.iloc[::5, :]
arr = df.to_numpy()
ppdf = pp.DataFrame(arr, var_names = var_names, datatime = np.arange(len(arr)))
"""tp.plot_timeseries(ppdf)
plt.show()
"""
parcorr = ParCorr(significance='analytic')
pcmci = PCMCI(
    dataframe= ppdf, 
    cond_ind_test=parcorr,
    verbosity=1)
"""correlations = pcmci.get_lagged_dependencies(tau_max=10, val_only=True)['val_matrix']
lag_func_matrix = tp.plot_lagfuncs(val_matrix=correlations, setup_args={'var_names':var_names, 'x_base':1, 'y_base':.5})
plt.show()"""
results = pcmci.run_pcmci(tau_max=12, pc_alpha=None)
print("p-values")
print (results['p_matrix'].round(3))
print("MCI partial correlations")
print (results['val_matrix'].round(2))
