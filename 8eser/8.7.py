import sys
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from numba import jit

def func(x) :
	return np.sin(x)

def integral_MC(f, a, b, N_evt) :
	x_random = np.random.uniform(a, b, N_evt)
	mean_f = np.mean(f(x_random))
	integer = (b-a)*mean_f
	uncertainty = np.std(x_random)/np.sqrt(N_evt)
	return integer, uncertainty
	
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
	N_max = int(sys.argv[1])
	arrayerr = []
	arrayerr2 = []
	
	n = 10
	n_events = []
	while n<=N_max :
		n_events.append(n)
		arrayerr.append(integral_MC(func,0, np.pi, n))
		n += 50
		
	n = 10
	while n <= N_max :
		arrayerr2.append(integral(func, 0, np.pi, -1, 1 , n))
		n += 50
		
	print(np.size(arrayerr))
	print(np.size(arrayerr2))
	y_coord = list(arrayerr[i][0] for i in range(len(arrayerr)))
	y_coord2 = list(arrayerr2[i][0] for i in range(len(arrayerr2)))
	y_err = list(arrayerr[i][1] for i in range(len(arrayerr)))
	y_err2 = list(arrayerr2[i][1] for i in range(len(arrayerr2)))
	fig, ax = plt.subplots(1,1)
	x_coord = np.linspace(0, 2*np.pi, 1000)
	plt.plot(x_coord, func(x_coord), color = 'blue', label = 'sinx')
	plt.fill_between(x_coord, func(x_coord), color = 'red', alpha = 0.5)
	plt.scatter(np.random.uniform(0,2*np.pi, N_max), np.random.uniform(-1,1, N_max), alpha = 0.5, color = 'green', label= 'punti randomici')
	plt.legend()
	plt.show()
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=n_events, y = y_coord , mode = 'markers', name = 'stima integrale con crude MC', error_y = dict(type = 'data' , array = y_err , color = 'purple', thickness = 1.5, width = 3), marker = dict(color = 'green', size = 8)))
	fig.add_trace(go.Scatter(x=n_events, y = y_coord2 , mode = 'markers', name = 'stima integrale con hit or miss', error_y = dict(type = 'data' , array = y_err2 , color = 'brown', thickness = 1.5, width = 3), marker = dict(color = 'red', size = 8)))
	fig.show()
	
   	


if __name__ == "__main__":
    main()
