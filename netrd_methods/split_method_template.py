import netrd
import numpy as np
import pandas as pd
import networkx as nx

reconstructor = netrd.reconstruction.ConvergentCrossMapping()
method = "ConvergentCrossMapping"
file = "split_results/" + method + ".csv"

df = pd.read_csv('collation_revised.csv')
df.drop(df.columns[[0]], axis = 1, inplace = True)
df.drop(df.columns[[0]], axis = 1, inplace = True)
df.drop(columns = ['AU', 'LC', 'RI'], inplace = True)
df = df.dropna()
"""
To find number of missing values do df.isnull().sum()
Number of missing values for each geyser:
AU            211919
BE               280
CA               143
DE               209
DO               198
GR             18799
LC             89622
LN               187
LS               196
OF              1433
PM               130
PT              1319
RI             60418
"""

df_list = []
# Use print(len(df.index)) to find number of rows
# 7521 is number of rows per data frame 
# This changes depending on which columns we drop.
for i in range(100):
    shrek = 7521*i
    donkey = shrek + 7521
    df_list.append(df.iloc[shrek:donkey])
np_list = []
for dataframe in df_list:
    np_list.append(np.transpose(dataframe.to_numpy()))
res_list = []
for arr in np_list:
    G = reconstructor.fit(arr, tau = 60)
    res_list.append(nx.to_numpy_matrix(G))
shrektrix = res_list[0]
for i in range(1,100):
    shrektrix = np.add(shrektrix, res_list[i])
print(shrektrix)
print(np.divide(shrektrix, 100))
shrektrix = np.divide(shrektrix, 100)
shrekdf = pd.DataFrame(shrektrix, columns = ["BE", "CA", "DE", "DO", "GR", "LN", "LS", "OF", "PT", "PM"])
shrekdf.insert(loc=0, column='Names', value=["BE", "CA", "DE",	"DO",	"GR",	"LN",	"LS",	"OF",	"PT",	"PM"])
shrekdf.set_index('Names', inplace=True)
shrekdf.to_csv(file)

"""BE CA DE	DO	GR	LN	LS	OF	PT PM are the current geysers in use"""
"""AU	BE	CA	DE	DO	GR	LC	LN	LS	OF	PT	RI PM"""