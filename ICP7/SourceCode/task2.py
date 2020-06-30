import requests
from bs4 import BeautifulSoup
html = requests.get('https://en.wikipedia.org/wiki/Google')
soup = BeautifulSoup(html.content, "html.parser")
text = soup.get_text()
print(text)
