# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma") #muutoksia tehty

x = int(input("luku 1: "))
y = int(input("luku 2: "))
<<<<<<< HEAD
print(f"Lukujen {x} ja {y} summa on {summa(x, y)}")
print(f"Lukujen {x} ja {y} erotus on {erotus(x, y)}") #näihinkin muutoksia
=======
print(f"{x} + {y} = {summa(x, y)}")
print(f"{x} - {y} = {erotus(x, y)}") #näitä muuteltiin
>>>>>>> main

logger("lopetetaan")
print("goodbye!") #lisäys

#täällähän tapahtuu vaikka ja mitä
