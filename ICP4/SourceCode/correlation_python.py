# Correlation
import pandas as pd

dataset = pd.read_csv("train_preprocessed.csv")
x = dataset['Survived'].corr(dataset['Sex'])
print('Correlation is : ', x)

# second method for categorical
y =dataset[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)
print(y)
