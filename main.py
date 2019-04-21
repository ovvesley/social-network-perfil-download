import requests
from bs4 import BeautifulSoup
import json
#username = raw_input('Digite o perfil do usuario')
username = 'john'

r = requests.get('https://facebook.com/' + username + '/photos')
s = requests.Session()
s.post('https://facebook.com/' + username + '/photos', acessKey)
print(r.url)
soup = BeautifulSoup(r.content, 'html.parser')


fotos = soup.find_all(class_= 'uiMediaThumbImg')
print(fotos)
for itema in fotos:
    print(itema)


    
#print(lista)

#print(soup.prettify())
