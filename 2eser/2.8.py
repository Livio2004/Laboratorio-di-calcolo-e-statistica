import sys 
import numpy as np 
import math 
import matplotlib.pyplot as plt
import time as tm

def func(x,A,B) :
	return np.sin(x-A)+B
	
def func1(x,C,D):
	return np.cos(x*C)*D
def main () :
	A = float(input('inserisci il parametro A:'))
	B = float(input('inserisci il parametro B:'))
	C = float(input('inserisci il parametro C:'))
	D = float(input('inserisci il parametro D:'))
	fig, ax = plt.subplots(nrows = 1, ncols=1)
	x_coord = np.linspace(0,2*np.pi, 50)
	y_coord1 = np.sin(x_coord)
	y_coord2 = np.cos(x_coord)
	ax.plot(x_coord, y_coord1, 'r--',x_coord, y_coord2, 'bs')
	ax.set_title('Comparing trigonometric function', size = 14)
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	
	
	
	y_coord3 = func(x_coord, A, B)
	ax.plot(x_coord, y_coord3, 'g^')
	
	y_coord4 = func1(x_coord, C, D)
	ax.plot(x_coord, y_coord4, 'b--')
	plt.show()
	
	



if __name__ == "__main__":
  main ()
