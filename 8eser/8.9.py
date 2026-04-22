import sys
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from numba import jit

def func(x, mu = 0, sigma = 1) :
	return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-((x - mu)**2) / (2 * sigma**2))


def integral(f, xmin, xmax, ymin, ymax , N_evt) :
	x_coord = np.random.uniform(xmin, xmax, N_evt)
	y_coord = np.random.uniform(ymin, ymax, N_evt)
	f_coord = f(x_coord)
	nhits = np.sum((y_coord>=0) & (y_coord<=f_coord))-np.sum((y_coord<0) & (y_coord>f_coord))
	if nhits < 0 :
		nhits = abs(nhits)
	area = (xmax -xmin)*(ymax -ymin)
	integer = area*(nhits/N_evt)
	uncertainty = np.sqrt((np.power(area,2)*(nhits/N_evt)*(1-nhits/N_evt))/N_evt)
	return integer, uncertainty
				
			

def main():
	if len(sys.argv) != 2 :
		raise ValueError('Inserisci solo nmax eventi')
	N_evt = int(sys.argv[1])
	mu = 0 
	sigma = 1
	ks = range(1,6)
	results = []
	for k in ks :
		xmin, xmax = -k*sigma, k*sigma
		integer, uncertainty = integral(func, xmin, xmax, 0 , func(mu) , N_evt)
		results.append((k,integer, uncertainty))
		
	print("ksigma | estimated integral | uncertainty")
	for k, integer , uncertainty in results :
		print(f"{k}sigma | {integer : .6f} | +- {uncertainty : .6f}")
	x = np.linspace(-5*sigma, 5*sigma, 1000)
	y = func(x)
	plt.figure(figsize=(10,6))
	plt.plot(x, y, label = 'Gaussian pdf', color = 'red', lw = 2)
	colors = plt.cm.viridis(np.linspace(0.2,1, len(ks)))
	for k, color in zip(reversed(ks), reversed(colors)) :
		x_fill = np.linspace(-k*sigma, k*sigma)
		y_fill = func(x_fill)
		plt.fill_between(x_fill, y_fill, 0, color = color , alpha = 0.3, edgecolor = 'black', label = f"+-{k}sigma")
		
	plt.title('Hit or miss per pdf gaussiana')
	plt.xlabel('x')
	plt.ylabel("f(x)")
	plt.legend()
	plt.grid(alpha= 0.4)
	plt.show()
	
   	


if __name__ == "__main__":
    main()
