# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma") #muutoksia tehty

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{x} + {y} = {summa(x, y)}")
print(f"{x} - {y} = {erotus(x, y)}") #näitä muuteltiin

logger("lopetetaan")
print("goodbye!") #lisäys
