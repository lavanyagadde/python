import requests
from bs4 import BeautifulSoup
html = requests.get('https://en.wikipedia.org/wiki/Deep_learning')
soup = BeautifulSoup(html.content, "html.parser")
print('Title of the webpage : ', soup.title.string) # printing the title of the page
print('All the a tags: ', soup.find_all('a'))   # displaying all 'a' tags
with open('output.txt', 'w') as f:              # opening the file to write the data
    for link in soup.find_all('a'):
        f.write(str(link.get('href')) + "\n")   # getting all the href and storing them in the file


