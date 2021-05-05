import netrd
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('collation.csv')
df.drop(df.columns[[0]], axis = 1, inplace = True)
df.drop(df.columns[[0]], axis = 1, inplace = True)
df.drop(columns = ['AU', 'LC', 'RI'], inplace = True)
df = df.dropna()
df = df.iloc[::100, :]
print(df.head())
arr = df.to_numpy()
arr = np.transpose(arr)
print(arr[0:10])
print(arr.shape)
reconstructor = netrd.reconstruction.ConvergentCrossMapping()
G = reconstructor.fit(arr, tau = 1)
print(list(G.neighbors(1)))
plt.subplot(121)
nx.draw_kamada_kawai(G, with_labels=True, font_weight='bold')
res = nx.to_numpy_matrix(G)
"""res.columns = ["BE", "CA", "DE",	"DO",	"GR",	"LN",	"LS",	"OF",	"PT",	"PM"]
res.insert(loc=0, column='Names', value=["BE", "CA", "DE",	"DO",	"GR",	"LN",	"LS",	"OF",	"PT",	"PM"])
res.set_index('Names', inplace=True)
print(res)
res.to_csv("CCM_test.csv")"""
print(res)
res2 = reconstructor.results['correlation_matrix']
print(res2)
res3 = reconstructor.results['pvalues_matrix']
print(res3)
res4 = reconstructor.results['weights_matrix']
print(res4)
"""plt.show()
plt.subplot(122)
g = nx.DiGraph(res)
nx.draw_kamada_kawai(g, with_labels=True, font_weight='bold')
plt.show()"""
"""BE CA DE	DO	GR	LN	LS	OF	PT	PM"""
"""AU	BE	CA	DE	DO	GR	LC	LN	LS	OF	PM	PT	RI"""

