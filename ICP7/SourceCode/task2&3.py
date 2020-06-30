# task 2: Extract the following web URL text using BeautifulSoup
import requests
from bs4 import BeautifulSoup
html = requests.get('https://en.wikipedia.org/wiki/Google')
soup = BeautifulSoup(html.content, "html.parser")

# task3: Save it in input.tx
with open('input.txt', 'w') as file:
    for text1 in soup.find_all('p'):
        file.write(str(text1.text))





