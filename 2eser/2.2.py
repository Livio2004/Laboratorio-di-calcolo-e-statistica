import sys 
import numpy as np 
import math 
import matplotlib.pyplot as plt
def main () :
	array = np.arange(1,101)
	print(array)
	farray = np.cumsum(array)
	print(farray)
	return
		

if __name__ == "__main__":
  main ()
