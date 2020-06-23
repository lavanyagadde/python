# Multiple Regression for the “wine quality” dataset
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

# reading file data using pd
quality_dataset = pd.read_csv('winequality-red.csv')

# Finding the null values
nulls = pd.DataFrame(quality_dataset.isnull().sum())
nulls.columns = ['NullCount']
nulls.index.name = 'Feature'
print('Finding missing values: ', nulls)
# If there are null values need to handle them by using dropna() but here there are no null values

# finding the top 3 most correlated features to the target label(quality)
numeric_features = quality_dataset.select_dtypes(include=[np.number])
corr = numeric_features.corr()
highest = corr['quality'].sort_values(ascending=False)[:4]
print('Top 3 most correlated features to the quality',highest)

# splitting the data into train and test data
x_train = quality_dataset.drop("quality", axis=1)
y_train = quality_dataset['quality']
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=0)

# multiple linear regression
lr = linear_model.LinearRegression()
# training the data to fit the model
model = lr.fit(x_train,y_train)
# predicting the model
y_pred = model.predict(x_test)
# Evaluating the model using RMSE and R2 score
print('Root Mean Squared Error : ',mean_squared_error(y_test, y_pred))
print('R Squared score : ',r2_score(y_test,y_pred))



