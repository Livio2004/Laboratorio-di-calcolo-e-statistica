import sys 
import numpy as np 
import math 
import matplotlib.pyplot as plt
def main () :
	array = np.linspace(2, 50, 25) #oppure arange(2,101, 2)
	print(array)
	array2 = np.linspace(1, 49, 25) #oppure arange(1,100, 2)
	print(array2)
	array_sum = array + array2
	print(array_sum)
	return
		

if __name__ == "__main__":
  main ()
