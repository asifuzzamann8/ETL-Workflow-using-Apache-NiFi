#!/usr/bin/python3

#import sklearn
import sys
import pandas as pd
import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
from pandas import DataFrame
#import datetime as dt

file = pd.read_csv(sys.stdin)
#file.info()
#file.head()
#file.groupby(['label']).size()

file['Ransomware']=list(map(int, file['label'].str.contains('Crypt')))

file.to_csv(sys.stdout, index=False)
