import numpy as np 
import matplotlib.pyplot as plt
import random
import time  #Non dipende dalla funzione ma la lunghezza dell'intervallo diviso la precisione e la bisezione ricorsiva è la più lenta 
def f(x) :
	return np.cos(x)

def bisezione(xmin, xmax, f, prec = 0.0001 , max_attempts = 10000) : #uso un numero massimo di attempt come check
	if f(xmin)*f(xmax) >= 0 :
		raise ValueError("Non c'è nessuno zero nell'intervallo compatto o la funzione agli estremi dell'intervallo non ha segni opposti ")
		
	i = 0
	while (i< max_attempts and (xmax - xmin) > prec) :
		xave = (xmax + xmin)/2
		if f(xmin)*f(xave) > 0 :
			xmin = xave
		else :
			xmax = xave
			
		i += 1
		
	return (xmax+xmin)/2
	
def bisezione_ricorsiva(xmin, xmax, f, prec = 0.0001) :
	if f(xmin)*f(xmax) >= 0 :
		raise ValueError("Non c'è nessuno zero nell'intervallo compatto o la funzione agli estremi dell'intervallo non ha segni opposti ")
	xave = (xmin+xmax)/2
	if (xmax-xmin) < prec :
	 	return xave
	
	elif f(xmin)*f(xave) > 0 : 
		return bisezione_ricorsiva(xave, xmax, f)
	else : 
		return bisezione_ricorsiva(xmin, xave, f)
		


def main():
	root = bisezione(0,4,f)
	print(bisezione(0,4, f))
	print(bisezione_ricorsiva(0,4, f))
	time1 = time.time()
	bisezione(0,4, f)
	time2 = time.time()
	print('Tempo funzione non ricorsiva :', time2-time1)
	time3 = time.time()
	bisezione_ricorsiva(0,4, f) 
	time4 = time.time()
	print('Tempo funzione ricorsiva:', time4-time3)
	fig, ax = plt.subplots(1,1)
	x = np.linspace(-1,4,10000)
	ax.plot(x, f(x), lw = 2, color = 'red', label = 'funzione $y = \cos x$')
	ax.plot(root, f(root), 'go', label = 'zero della funzione')
	plt.axhline(0, color = 'grey', linestyle = '--')
	ax.set_xlim(-1,4)
	plt.legend()
	plt.show()
	
	
	
	
	
	



if __name__ == '__main__' :
	main()
