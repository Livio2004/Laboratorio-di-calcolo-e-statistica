import numpy as np 
import matplotlib.pyplot as plt
import random
import time  #Non dipende dalla funzione ma la lunghezza dell'intervallo diviso la precisione e la bisezione ricorsiva è la più lenta 
def f(x) :
	return x**2 + 7.3*x + 4

def extrema(f, xmin, xmax, prec = 0.0001, max_attempts = 10000) :
	phi = (np.sqrt(5)-1)/2
	x1 = xmin + phi*(xmax-xmin)
	x2 = xmin + (1-phi)*(xmax-xmin)
	i = 0
	while (abs(xmax-xmin)>prec and i <max_attempts) :
		if f(x2) >f(x1) :
			xmin = x2
			x1 = xmin + phi*(xmax-xmin)
			x2 = xmin + (1-phi)*(xmax-xmin)
		else :
			xmax = x1
			x2 = xmin + (1-phi)*(xmax-xmin)
			x1 = x1 = xmin + phi*(xmax-xmin)
			
		i += 1
	return (xmin+xmax)/2
	
def extrema2(f, xmin, xmax, prec = 0.0001, max_attempts = 10000) :
	phi = (np.sqrt(5)-1)/2
	x1 = xmin + phi*(xmax-xmin)
	x2 = xmin + (1-phi)*(xmax-xmin)
	i = 0
	while (abs(xmax-xmin)>prec and i <max_attempts) :
		if f(x2)>f(x1) :
			xmin = x2
			x2 = x1
			x1 = phi*(xmax-xmin)+xmin
		else :
			xmax = x1
			x1 = x2
			x2 = xmin + (1-phi)*(xmax-xmin)
			
			
		i += 1
	return (x1+x2)/2
	
	
def recursive_extrema(f, xmin, xmax, prec = 0.0001) :
	phi = (np.sqrt(5)-1)/2
	x1 = xmin + phi*(xmax-xmin)
	x2 = xmin + (1-phi)*(xmax-xmin)
	if (xmax-xmin)<prec :
		return (xmax+xmin)/2
	elif f(x2)<f(x1) : 
		return recursive_extrema(f, x2, xmax, prec = 0.0001)
	else :
		return recursive_extrema(f, xmin, x1, prec = 0.0001)
			
			
	
#secondo pieva -3.82

def main():
	print(extrema(f, -10, 0)) 
	print(extrema2(f,-10,0))
	print(recursive_extrema(lambda x : (-1)*x**2 + 7.3*x + 4, 0, 10))
	time1 = time.time()
	extrema(f, -10, 0)
	time2 = time.time()
	print('Tempo funzione non ricorsiva :', time2-time1)
	time3 = time.time()
	extrema2(f,-10,0)
	time4 = time.time()
	print('Tempo funzione con a = b:', time4-time3)
	root = extrema(f, -10, 0)
	x = np.linspace(-20,15,10000)
	fig,ax = plt.subplots(1,1)
	ax.plot(x, f(x), lw = 2, color = 'red', label = 'funzione')
	ax.plot(root, f(root), 'go', label = 'punto di minimo')
	plt.axhline(min(f(x)), color = 'grey', linestyle = '--')
	ax.set_xlim(-10,0)
	ax.set_ylim(-20,0)
	plt.legend()
	plt.show()
	
	
	
	
	
	



if __name__ == '__main__' :
	main()
