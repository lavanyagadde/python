import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# reading the dataset
glass_data = pd.read_csv('glass.csv')
# x_train = glass_data[['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe']]
x_train = glass_data.drop("Type", axis=1)
y_train = glass_data['Type']
# splitting train and test data using train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=0)

# Train the model using the training sets
svc = SVC()
svc.fit(x_train, y_train)
y_pred = svc.predict(x_test)
# Classification report is used to measure the quality of predictions using classification algorithm and accuracy
qual_report = classification_report(y_test, y_pred)
print(qual_report)
print("SVM accuracy is: ", accuracy_score(y_test, y_pred)*100)



