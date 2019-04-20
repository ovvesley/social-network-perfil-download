import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.google.com')


soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
