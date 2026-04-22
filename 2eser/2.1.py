import sys 
import numpy as np 
import math 
import matplotlib.pyplot as plt
def main () :
	array = np.array([1,2,3,4])
	print (array)	
	array2 = np.zeros(10)
	print(array2)
	array3 = np.empty(10)
	print(array3)
	array4 = np.arange(1,10,2)
	print(array4)
	array5 = np.linspace(1,10, 8)
	print(array5)
	array6 = np.ones(5)
	print(array6)

if __name__ == "__main__":
  main ()
