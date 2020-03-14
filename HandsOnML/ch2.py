# import os 
# import tarfile
# import pandas as pd 
# from six.moves import urllib

# DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/" 
# HOUSING_PATH = os.path.join("datasets", "housing") 
# HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from tuna import split_train_test

csv_path = 'C:/Users/BEAR/Documents/GitHub/python_practice/HandsOnML/RawData/housing.csv'
housing = pd.read_csv(csv_path)

print(housing.head)
# print(housing['ocean_proximity'].value_counts())
# print(housing.describe())

# housing.hist(bins=50, figsize=(20,15))
# plt.show()

# shuffled_indices = np.random.permutation(len(housing))
# print(shuffled_indices)

# def split_train_test(data, test_ratio):
#     shuffled_indices = np.random.permutation(len(data))
#     test_set_size = int(len(data) * test_ratio)
#     test_indices = shuffled_indices[:test_set_size]
#     train_indices = shuffled_indices[test_set_size:]
#     return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = split_train_test(housing, 0.2)

print(len(train_set), "tranin + ", len(test_set), "test")

# tuna.fish()
# 
# def fish():
#     print("I am Happy tuna")

# fish()




