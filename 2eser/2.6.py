import sys 
import numpy as np 
import math 
import matplotlib.pyplot as plt
import time as tm
from libreria1 import percentage25, percentage75, percentage

def main () :
	N = int(input('Inserisci dimensione array:'))
	P = int(input('Inserisci percentuale per calcolo:'))
	if cent>100 :
		print('la percentuale non può essere naggiore di 100')
		sys.exit()
	else :
		array = np.sort(np.random.randint(200, size = (N)))
		print(array)
		print(percentage25(array, N))
		print(percentage75(array, N))
		print(percentage(array, N, P))
		return
if __name__ == "__main__":
  main ()
	

