import matplotlib.pyplot as plt
import numpy as np
import sys 
from libreria import lavoro 

def main() :
	istogramma = lavoro('eventi_gauss.txt')
	istogramma.isto('Ex_3.6.png')
	print(istogramma.dato())
	print(istogramma.varianza2())
	
			
if __name__ == "__main__":
	main ()
