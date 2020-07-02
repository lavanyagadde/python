# task2 : Change the data source to Breast Cancer
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

dataset = pd.read_csv("breastcancer.csv")
total_cols=len(dataset.axes[1])
print(total_cols)
print(dataset.dtypes)
# Converting a categorical feature
le = LabelEncoder()
x_train = dataset.iloc[:, 2:31]
y_train = le.fit_transform(dataset['diagnosis'])
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train,
                                                    test_size=0.25, random_state=87)
np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(20, input_dim=29, activation='relu')) # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(x_train, y_train, epochs=100,
                                     initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(x_test, y_test))