# finding and removing outliers
# importing packages
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# reading file data using pd
house_dataset = pd.read_csv('train.csv')
print(house_dataset.SalePrice.describe())
print(house_dataset.GarageArea.describe())
# scatter plot to find outlier
plt.scatter(house_dataset['GarageArea'],house_dataset['SalePrice'])
plt.xlabel('Garage Area')
plt.ylabel('Sales Price')
plt.title('Scatter plot to before finding outliers')
plt.show()

# removing outliers using z score
# Z-Score tells how far a point is from the mean of dataset in terms of standard deviation
z_scores = stats.zscore(house_dataset[['GarageArea', 'SalePrice']])
abs_z_scores = np.abs(z_scores)
# An absolute value of z score which is above 3 is termed as an outlier
filtered_entries = (abs_z_scores < 3).all(axis=1)
house_new = house_dataset[filtered_entries]

# Scatter plot after removing outliers
plt.scatter(house_new['GarageArea'], house_new['SalePrice'], c='g')
plt.xlabel('Garage Area')
plt.ylabel('Sales Price')
plt.title('Scatter plot after removing outliers')
plt.show()





