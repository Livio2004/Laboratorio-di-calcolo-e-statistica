import matplotlib.pyplot as plt
import numpy as np
import sys 
from scipy.stats import expon

def GRN(items,seed, A, C, M) :
	x = seed
	randlist = []
	for i in range(items-1) :
		x = (A*x + C) % M
		randlist.append(x)
	return randlist
		
		
	

def main() :
	items = int(input('Inserisci quanti numeri casuali vuoi:'))
	seed = float(input('Quale seed vuoi?'))
	A = 214013
	C = 2531011
	M = 2147483647
	
	print(GRN(items, seed, A, C, M))
	
			
if __name__ == "__main__":
	main ()
