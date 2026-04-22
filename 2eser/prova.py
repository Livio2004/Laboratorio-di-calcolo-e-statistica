import sys 
import numpy as np 
import math 
import matplotlib.pyplot as plt
def main () :
	array = np.array([1,2,3,4])
	array2 = np.zeros(10)
	array3 = np.empty(10)
	array4 = np.arange(1,10,2)
	tot = np.sum(array4) #c'è anche cumsum e cumprod
	fig, ax = plt.subplots(nrows = 1, ncols = 1)
	x_coord = np.linspace(0, 2*np.pi, 10000)
	y_coord = np.sin (x_coord)
	ax.plot(x_coord, y_coord, label = 'sin(x)') #quando plotti devi plottare sull'ax
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.legend('grafico di prova')
	plt.show()
	return

if __name__ == "__main__":
  main ()
