from nltk.corpus import stopwords
from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

tfidf_Vect = TfidfVectorizer()
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
# print(tfidf_Vect.vocabulary_)
clf = MultinomialNB()
clf.fit(X_train_tfidf, twenty_train.target)

twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)

predicted = clf.predict(X_test_tfidf)

score = metrics.accuracy_score(twenty_test.target, predicted)
print('Naive Byes accuracy score : ', score)

# task1: changing classifier to SVM
from sklearn.svm import SVC
# building SVM model
svc = SVC()
svc.fit(X_train_tfidf, twenty_train.target)
pred = svc.predict(X_test_tfidf)
score1 = metrics.accuracy_score(twenty_test.target, pred)
print('SVM accuracy score', score1)

# change the tfidf vectorizer to use bigram

tfidf_Vect_bigram = TfidfVectorizer(ngram_range=(1, 2))

X_train_tfidf_bigram = tfidf_Vect_bigram.fit_transform(twenty_train.data)

X_test_tfidf_bigram = tfidf_Vect_bigram.transform(twenty_test.data)

# building the model
svc.fit(X_train_tfidf_bigram, twenty_train.target)
pred1 = svc.predict(X_test_tfidf_bigram)
score2 = metrics.accuracy_score(twenty_test.target, pred1)

# checking how the accuracy changes for svm
print('SVM accuracy score when bigram is used: ', score2)

# Set argument stop_words='english' and see how accuracy changes
stop_words = set(stopwords.words('english'))

tfidf_Vect_stopwords = TfidfVectorizer(ngram_range=(1, 2), stop_words = 'english')

X_train_tfidf_stopwords = tfidf_Vect_stopwords.fit_transform(twenty_train.data)

X_test_tfidf_stopwords = tfidf_Vect_stopwords.transform(twenty_test.data)
# building the model
svc.fit(X_train_tfidf_stopwords, twenty_train.target)
pred2 = svc.predict(X_test_tfidf_stopwords)
score3 = metrics.accuracy_score(twenty_test.target, pred2)
print('SVM accuracy after set stopwords =''English', score2)