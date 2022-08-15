import numpy as np
import pandas as pd

# Read and convert csv to dataframe
table = "/data//info.csv"
df_cf = pd.read_csv(table, header=0)

# Nunber of Wells  by type
h_prod = df_cf['Horizontales'].values
d_prod = df_cf['Direccionales'].values
v_prod = df_cf['Vertical'].values

# Number of Workvers by type
upz = df_cf['upsizing'].values
acid = df_cf['acidizing'].values
frac = df_cf['fracturing'].values

#define inputs for qarps
t = df_cf['año'].values

# Oil production rate
def qarps(t,qi,di,b = 0):
    return qi / (np.abs((1 + b * di * (t*365)))**(1/b))



