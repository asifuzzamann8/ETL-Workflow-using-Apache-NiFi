# !/bin/bash

/usr/bin/python3 /home/hadoop/python_scripts/nifi_uci.py

export HADOOP_USER_NAME=hadoop
/home/hadoop/hadoop-3.1.2/bin/hadoop dfs -put -f /home/hadoop/nifi_data/BitcoinHeistData_v2.csv /user/hive/uci_ransomware_ext
