import pandas as pd
import matplotlib
from pyupset.visualisation import plot

p07 = pd.read_csv('30765_0107.csv', sep='\t')
p08 = pd.read_csv('30765_0108.csv', sep='\t')
p09 = pd.read_csv('30765_0109.csv', sep='\t')
p10 = pd.read_csv('30765_0110.csv', sep='\t')
p11 = pd.read_csv('30765_0111.csv', sep='\t')

plot({'2019-01-07': p07, '2019-01-08': p08, '2019-01-09': p09,'2019-01-10': p10,'2019-01-11': p11}, unique_keys=['machine_guid'])

current_figure = matplotlib.pyplot.gcf()
current_figure.suptitle('Unique machine guids reported by Signature 30765 "System Infected: Miner.Bitcoinminer Activity 7"', fontsize=16)
current_figure.savefig("result.png")
