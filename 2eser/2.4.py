import sys 
import numpy as np 
import math 
import matplotlib.pyplot as plt
import time as tm
def main () :
	N = int(input('Inserisci dimensione lista:'))
	array = np.arange(0,N) #oppure arange(2,101, 2)
	print(array)
	array2 = np.arange(0,N) #oppure arange(1,100, 2)
	print(array2)
	time1 = tm.time()
	arraysum = array+array2
	time2 = tm.time()
	print('Tempo occupato:', time2-time1, 'ms')
	print(arraysum) 
	list_1 = list(range(N))
	list_2 = list(range(N))
	times1 = tm.time()
	arraysum_1 = list(range(N))
	for i in range(0,N) :
		arraysum_1[i] = list_1[i]+list_2[i]
	times2 = tm.time()
	print('Tempo occupato:', times2-times1, 'ms')
	print(arraysum_1)
		
		
	return
		

if __name__ == "__main__":
  main ()
