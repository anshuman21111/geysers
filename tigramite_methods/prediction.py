
# Imports
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import sklearn

import tigramite
from tigramite import data_processing as pp
from tigramite import plotting as tp
from tigramite.pcmci import PCMCI
from tigramite.independence_tests import ParCorr, GPDC, CMIknn, CMIsymb
from tigramite.models import LinearMediation, Prediction

import pandas as pd

df = pd.read_csv('collation.csv')
df.drop(df.columns[[0]], axis = 1, inplace = True)
df.drop(df.columns[[0]], axis = 1, inplace = True)
df.drop(columns = ['AU', 'LC', 'RI'], inplace = True)
var_names = df.columns
df = df.dropna()
df = df.iloc[::10, :]
arr = df.to_numpy()
ppdf = pp.DataFrame(arr, var_names = var_names)

T, N = arr.shape
pred = Prediction(dataframe=ppdf,
        cond_ind_test=ParCorr(),   #CMIknn ParCorr
        prediction_model = sklearn.linear_model.LinearRegression(),
#         prediction_model = sklearn.gaussian_process.GaussianProcessRegressor(),
        # prediction_model = sklearn.neighbors.KNeighborsRegressor(),
    data_transform=sklearn.preprocessing.StandardScaler(),
    train_indices= range(int(0.8*T)),
    test_indices= range(int(0.8*T), T),
    verbosity=1
    )
target = [0,1,2,3,4,5,6,7,8,9]
tau_max = 6
steps_ahead = 3

all_predictors = pred.get_predictors(
                  selected_targets=[target],
                  steps_ahead=steps_ahead,
                  tau_max=tau_max,
                  pc_alpha=None
                  )
link_matrix = np.zeros((N, N, tau_max + 1), dtype='bool')
for j in target:
    for p in all_predictors[j]:
        link_matrix[p[0], j, abs(p[1])] = 1

pred.fit(target_predictors=all_predictors, 
                selected_targets=target,
                    tau_max=tau_max)

predicted = pred.predict(target)
for i in range(0, 10):
    plt.figure(i+1)
    true_data = pred.get_test_array()[0]
    plt.scatter(true_data, predicted[i])
    plt.title(r"Geyser %s: NRMSE = %.2f" % (var_names[i], np.abs(true_data - predicted[i]).mean()/true_data.std()))
    plt.plot(true_data, true_data, 'k-')
    plt.xlabel('True test data')
    plt.ylabel('Predicted test data')
    plt.savefig("figs/%s" %(var_names[i]))