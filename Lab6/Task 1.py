# all tasks
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def space():
    print('\n\n\n')


df = pd.read_csv('C:\\Users\\User\\Desktop\\NYC_Jobs.csv', sep=',')
print(df.columns, '\n')
# first 10 elements of ds
for i in range(10):
    print(df.iloc[i])
    print("**********************************************************************************")
# Agency for 10 elem
space()
print("AGENCY START HERE")
for i in range(10):
    print(df.loc[[i], 'Agency'])
space()
print("ALL AGENCIES")
print(df['Agency'])
space()
print("ALL BUSINESS TITLES ")
print(df['Business Title'])
space()
print("ALL WORKING LOCATIONS")
print(df['Work Location 1'])
space()
pvt = df.pivot_table(index=['Agency'], values='# Of Positions')
print(pvt)
pvt.plot.bar()
plt.show()
space()
df['median'] = df.groupby('Salary Range From')['Salary Range To'].transform(np.median)
gb = df.groupby('Work Location')
data1 = pd.DataFrame([df.loc[gb.groups[n], 'median'].values for n in gb.groups], index=gb.groups.keys())
data1 = data1.median(axis=1)
data1.plot()
plt.show()