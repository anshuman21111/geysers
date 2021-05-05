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
df = df.iloc[::1, :]
print(df.head())
arr = df.to_numpy()
arr = np.transpose(arr)
reconstructor = netrd.reconstruction.MarchenkoPastur()
G = reconstructor.fit(arr)
print(list(G.neighbors(1)))
# plt.subplot(121)
# nx.draw_kamada_kawai(G, with_labels=True, font_weight='bold')
res = nx.to_pandas_adjacency(G)
res.columns = ["BE", "CA", "DE",	"DO",	"GR",	"LN",	"LS",	"OF",	"PT",	"PM"]
res.insert(loc=0, column='Names', value=["BE", "CA", "DE",	"DO",	"GR",	"LN",	"LS",	"OF",	"PT",	"PM"])
res.set_index('Names', inplace=True)
# print(res)
res.to_csv("marchenko_pastur.csv")
# plt.show()

"""BE CA DE	DO	GR	LN	LS	OF	PT	PM"""
"""AU	BE	CA	DE	DO	GR	LC	LN	LS	OF	PM	PT	RI"""