#!Python3
import pandas as pd 
import openpyxl
import os 

files = {
    'AU': "0708_files/AU.csv",
    'BE': "0708_files/BE.csv",
    'CA': "0708_files/CA.csv",
    'DE': "0708_files/DE.csv",
    'DO': "0708_files/DO.csv",
    'GR': "0708_files/GR.csv",
    'LC': "0708_files/LC.csv",
    'LN': "0708_files/LN.csv",
    'LS': "0708_files/LS.csv",
    'OF': "0708_files/OF.csv",
    'PM': "0708_files/PM.csv",
    'PT': "0708_files/PT.csv",
    'RI': "0708_files/RI.csv",
}
dframes = {}
for geyser in files:
    path = files[geyser]
    df = pd.read_csv(path, parse_dates=[1])
    df.drop(df.columns[[0]], axis = 1, inplace = True)
    df['DateTime'] = df['DateTime'].dt.round('T')
    mask = (df['DateTime'] <= '2/1/2008 00:00:00')
    inv_mask = (df['DateTime'] > '2/1/2008 00:00:00')
    df0 = df.loc[mask]
    df1 = df.loc[inv_mask]
    print(df0.head())
    print(df0.tail())
    print(df1.head())
    print(df1.tail())
    dframes[geyser] = [df0, df1]
dfinal = pd.DataFrame()
i = 0
while i < 2:
    dtemp = pd.DataFrame()
    for geyser in dframes:
        df = dframes[geyser][i]
        print(df.head())
        print(dtemp.head())
        if geyser == 'AU':
            dtemp = df
        else:
            dtemp = pd.merge_ordered(dtemp, df)
    dfinal =pd.concat([dfinal, dtemp])
    i = i + 1
dfinal.to_csv("collation.csv")