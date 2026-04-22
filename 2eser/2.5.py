import sys 
import numpy as np 
import math 
import matplotlib.pyplot as plt
import time as tm
def main () :
	N = int(input('Inserisci dimensione array:'))
	array = np.sort(np.random.randint(200, size = (N)))
	print(array)
	print(np.median(array))
	if N%2 != 0 :
		s = array[int(N/2)]
		print('Il valore centrale è :', s)
	else :
		t = (array[int((N/2)-1)]+array[int(N/2)])/2
		print('Il valore centrale è :', t)

if __name__ == "__main__":
  main ()
