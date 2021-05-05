#!Python3
import pandas as pd 
import openpyxl
import os 

""" "AU": [
    "allgeysers_rawtemp/Aurum_Geyser/6_Finalized_Data/Aurum_Geyser_2007.xlsx",
    "allgeysers_rawtemp/Aurum_Geyser/6_Finalized_Data/Aurum_Geyser_2008.xlsx"],
"""
data = {
    
    "BE": [
    "allgeysers_rawtemp/Beehive_Geyser/6_Finalized_Data/Beehive_Geyser_2007.xlsx",
    "allgeysers_rawtemp/Beehive_Geyser/6_Finalized_Data/Beehive_Geyser_2008.xlsx"],

    "CA": [
    "allgeysers_rawtemp/Castle_Geyser/6_Finalized_Data/Castle_Geyser_2007.xlsx",
    "allgeysers_rawtemp/Castle_Geyser/6_Finalized_Data/Castle_Geyser_2008.xlsx"],

    "DE": [
    "allgeysers_rawtemp/Depression_Geyser/6_Finalized_Data/Depression_Geyser_2007.xlsx",
    "allgeysers_rawtemp/Depression_Geyser/6_Finalized_Data/Depression_Geyser_2008.xlsx"],

    "DO": [
    "allgeysers_rawtemp/Dome_Geyser/6_Finalized_Data/Dome_Geyser_2007.xlsx",
    "allgeysers_rawtemp/Dome_Geyser/6_Finalized_Data/Dome_Geyser_2008.xlsx"],

    "GR": [
    "allgeysers_rawtemp/Grand_Geyser/6_Finalized_Data/Grand_Geyser_South_Channel_2007.xlsx",
    "allgeysers_rawtemp/Grand_Geyser/6_Finalized_Data/Grand_Geyser_South_Channel_2008.xlsx"],

    "LN": [
    "allgeysers_rawtemp/Lion_Geyser/6_Finalized_Data/Lion_Geyser_2007.xlsx",
    "allgeysers_rawtemp/Lion_Geyser/6_Finalized_Data/Lion_Geyser_2008.xlsx"],

    "LC": [
    "allgeysers_rawtemp/LittleClub_Geyser/6_Finalized_Data/Little_Cub_Geyser_2007.xlsx",
    "allgeysers_rawtemp/LittleClub_Geyser/6_Finalized_Data/Little_Cub_Geyser_2008.xlsx"],

    "LS": [
    "allgeysers_rawtemp/LittleSquirt_Geyser/6_Finalized_Data/Little_Squirt_Geyser_2007.xlsx",
    "allgeysers_rawtemp/LittleSquirt_Geyser/6_Finalized_Data/Little_Squirt_Geyser_2008.xlsx"],

    "OF": [
    "allgeysers_rawtemp/OldFaithful_Geyser/6_Finalized_Data/OldFaithful_2007.xlsx",
    "allgeysers_rawtemp/OldFaithful_Geyser/6_Finalized_Data/OldFaithful_2008.xlsx"],

    "PT": [
    "allgeysers_rawtemp/Plate_Geyser/6_Finalized_Data/Plate_Geyser_2007.xlsx",
    "allgeysers_rawtemp/Plate_Geyser/6_Finalized_Data/Plate_Geyser_2008.xlsx"],

    "RI": [
    "allgeysers_rawtemp/Riverside_Geyser/6_Finalized_Data/Plume_Geyser_2007.xlsx",
    "allgeysers_rawtemp/Riverside_Geyser/6_Finalized_Data/Plume_Geyser_2008.xlsx"],
}
shrek = {
    "RI": ["allgeysers_rawtemp/Riverside_Geyser/6_Finalized_Data/Riverside_Geyser_2007.xlsx",
    "allgeysers_rawtemp/Riverside_Geyser/6_Finalized_Data/Riverside_Geyser_2008.xlsx"],
}
donkey = {
    "PM": [
    "allgeysers_rawtemp/Plume_Geyser/6_Finalized_Data/Plume_Geyser_2007.xlsx",
    "allgeysers_rawtemp/Plume_Geyser/6_Finalized_Data/Plume_Geyser_2008.xlsx"],
}
# Use this to cut out data from april 2007 to november 2008
"""df = pd.read_excel("allgeysers_rawtemp/Aurum_Geyser/6_Finalized_Data/Aurum_Geyser_2007.xlsx", "Sheet1")
df.columns = ['Unamed', 'DateTime', 'SerialNumber', 'AU']
df = df.drop(df.columns[[0,2]], axis = 1)
df['DateTime'] = pd.to_datetime(df['DateTime'])
mask = (df['DateTime'] >= '4/1/2007 00:00:00') & (df['DateTime'] < '11/1/2008 00:00:00')
print(df.loc[mask].head()) """

for geyser in donkey:
    df = pd.DataFrame()
    for path in donkey[geyser]:
        print(path)
        df0 = pd.read_excel(path, "Sheet1")
        df0.columns = ['Unamed', 'DateTime', 'SerialNumber', geyser]
        df = pd.concat([df, df0])
    try:
        df.columns = ['Unamed', 'DateTime', 'SerialNumber', geyser]
        df = df.drop(df.columns[[0,2]], axis = 1)
    except:
        df.columns = ['Unamed', 'DateTime', 'SerialNumber', geyser, 'Shrek']
        df = df.drop(df.columns[[0,2,4]], axis = 1)
    df['DateTime'] = pd.to_datetime(df['DateTime'])
    mask = (df['DateTime'] >= '4/1/2007 00:00:00') & (df['DateTime'] < '11/1/2008 00:00:00')
    df = df.loc[mask]
    df.to_csv("0708_files/"+geyser+".csv")