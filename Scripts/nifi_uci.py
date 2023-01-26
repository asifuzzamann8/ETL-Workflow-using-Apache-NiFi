#!/usr/bin/python3

import pandas as pd
import numpy as np
from pandas import DataFrame

file = pd.read_csv("/home/hadoop/nifi_data/BitcoinHeistData.csv")
#file.info()
#file.head()
#file.groupby(['label']).size()

file['Ransomware']=list(map(int, file['label'].str.contains('Crypt')))

file.to_csv("/home/hadoop/nifi_data/BitcoinHeistData_v2.csv", index=False)
