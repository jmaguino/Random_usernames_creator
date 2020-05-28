#This small program is used to create usernames from a list of random words.
#For this program, we will import the requests, random, and randint modules.
#We will use a url with the list of words.

#Este pequeno programa es usado para crear nombres de usuarios de uns lista de
#palabras al azar.
#Para el funcionamiento de este programa, importaremos los modulos requests
#(pedido), random (arbitrario), randint (numero entero arbitrario).

import requests
from random import randint

url = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'

r = requests.get(url)
text = r.text

individual_words = text.split()

random_number = randint(0,len(individual_words))

print(individual_words[random_number] + str(random_number))
