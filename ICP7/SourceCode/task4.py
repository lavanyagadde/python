# task 4: Apply the following on the “input.txt” and show output:
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, ne_chunk, ngrams
from nltk.tokenize import wordpunct_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# opening the file and reading the data from the file
with open('Input.txt', 'r') as text_file:
    read_data = text_file.read()

# a.Tokenization
# senetence Tokenization
stokens = nltk.sent_tokenize(read_data)
print('sentence stokes: ', stokens)
# words Tokenization
wtokens = nltk.word_tokenize(read_data)
print('words stokes: ', wtokens)

# b.POS
pos = nltk.pos_tag(wtokens)
print('part of the speech: ', pos)

# c.Stemming
# porter Stemmer
pStemmer = PorterStemmer()
print('Porter Stemmer: \n')
for i in wtokens:
    print(pStemmer.stem(i),end=' ')
print('\n***************')
# Lancaster Stemmer
lStemmer = LancasterStemmer()
print('Lancaster Stemmer: \n')
for i in wtokens:
    print(lStemmer.stem(i),end=' ')
print('\n***************')
# snowball Stemmer
sStemmer = SnowballStemmer('english')
print('Snowball Stemmber:\n')
for i in wtokens:
    print(sStemmer.stem(i),end=' ')

# d. Lemmatization
lemmatizer = WordNetLemmatizer()
print('\n Lemmatization : \n')
for i in wtokens:
    print(lemmatizer.lemmatize(str(i)),end=' ')

# e.Trigram
print("\nTrigrams :\n")
# trigram = []
# for x in wtokens:
#     trigram.append(list(ngrams(x, 3)))
# print(trigram)
trigrams = list(ngrams(wtokens,3))
print("trigrams:")
print(trigrams)

# f. Named Entity Recognition
print("Named Entity Recognition:")
print(ne_chunk(pos_tag(wordpunct_tokenize(read_data))))







