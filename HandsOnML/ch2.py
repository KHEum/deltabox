# import os 
# import tarfile
# import pandas as pd 
# from six.moves import urllib

# DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/" 
# HOUSING_PATH = os.path.join("datasets", "housing") 
# HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

# def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
#     if not os.path.isdir(housing_path):
#         os.makedirs(housing_path)
#     tgz_path = os.path.join(housing_path, "housing.tgz")    
#     urllib.request.urlretrieve(housing_url, tgz_path)    
#     housing_tgz = tarfile.open(tgz_path)    
#     housing_tgz.extractall(path=housing_path)    
#     housing_tgz.close()

# def load_housing_data(housing_path=HOUSING_PATH):
#     csv_path = os.path.join(housing_path, "housing.csv")
#     return pd.read_csv(csv_path) 


# housing = load_housing_data()
# housing.head()


import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import tuna as tn

csv_path = 'C:/Users/BEAR/Documents/GitHub/python_practice/HandsOnML/RawData/housing.csv'
housing = pd.read_csv(csv_path)

# print(housing.head)
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

tuna.fish()

# def fish():
#     print("I am Happy tuna")

# fish()

