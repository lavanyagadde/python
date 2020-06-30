# task1: Change the classifier in the given code to
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB

# Given Source Code
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
tfidf_Vect = TfidfVectorizer()
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
clf = MultinomialNB()
clf.fit(X_train_tfidf, twenty_train.target)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
predicted = clf.predict(X_test_tfidf)
score = metrics.accuracy_score(twenty_test.target, predicted)
print('Naive bayes accuracy score is : ', score)

# task1: a. SVM and seeing how accuracy changes
from sklearn.svm import SVC
svc = SVC()
svc.fit(X_train_tfidf, twenty_train.target)
pred = svc.predict(X_test_tfidf)
# accuracy score for SVM
score1 = metrics.accuracy_score(twenty_test.target, pred)
print('Accuracy score for SVM: ', score1)

# b.change the tfidf vectorizer to use bigram and see how the accuracy changes
tfidf_Vect_bigram = TfidfVectorizer(ngram_range=(1, 2))
X_train_tfidf_bigram = tfidf_Vect_bigram.fit_transform(twenty_train.data)
X_test_tfidf_bigram = tfidf_Vect_bigram.transform(twenty_test.data)
svc.fit(X_train_tfidf_bigram, twenty_train.target)
pred1 = svc.predict(X_test_tfidf_bigram)
score2 = metrics.accuracy_score(twenty_test.target, pred1)
print('Accuracy score after using bigram with SVM ', score2)

# c.Set argument stop_words='english' and see how accuracy changes
#
tfidf_Vect_stopwatch = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
X_train_tfidf_stopwatch = tfidf_Vect_stopwatch.fit_transform(twenty_train.data)
X_test_tfidf_stopwatch = tfidf_Vect_stopwatch.transform(twenty_test.data)
svc.fit(X_train_tfidf_stopwatch, twenty_train.target)
pred2 = svc.predict(X_test_tfidf_stopwatch)
score3 = metrics.accuracy_score(twenty_test.target, pred2)
print('Accuracy score after using stopwatch as english with SVM and bigram', score3)


