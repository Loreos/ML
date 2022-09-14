import pandas as pd
import os

datapath = os.path.join("../datasets","lifesat","")

# oecd_bli = pd.read_csv(datapath + "oecd_bli_2015.csv", thousands = ',')

oecd = pd.read_csv("datasets/lifesat/oecd_bli_2015.csv", thousands = ',')