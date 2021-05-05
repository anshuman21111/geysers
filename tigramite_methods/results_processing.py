import numpy as np
import re

f = open("results_sample.txt", "r")
r = open("results_step2.txt", "w")
lines = f.readlines()


for line in lines:
    shrek = re.sub("\s+", ",", line)
    donkey = re.sub("^(,)", "", shrek)
    fiona = re.sub("\[,", "[", donkey)
    r.write(fiona)
    r.write("\n")

