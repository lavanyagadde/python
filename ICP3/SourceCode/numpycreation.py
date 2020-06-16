import numpy as np

a = np.random.uniform(1, 20, 20)  # creating the random vector of size 20 having only float in the range 1-20
print('Random vector of size  20: \n', a)
b = a.reshape((4, 5))  # reshaping the array to 4 by 5
print('Reshaping the  array to 4 by 5: \n', b)
c = np.where(b == np.amax(b, axis=1).reshape(-1, 1), 0, b)  # replace the max in each row by 0(axis=1)
print('Replacing the  maximum in each row by 0: \n', c)


