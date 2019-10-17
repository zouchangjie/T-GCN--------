import pandas as pd
import numpy as np

data = pd.read_csv(r'data/sz_speed.csv')
data1 =np.mat(data,dtype=np.float32)
# max_value = np.max(data1)
# data1 = data1/max_value
print(data1[0])
