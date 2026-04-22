import sys
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from numba import jit

def func(x) :
	return np.sin(x)

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
	arrayerr = [integral(func, 0, np.pi, -1,1, x) for x in range(100,N_max)]
	y_coord = list(arrayerr[i][0] for i in range(len(arrayerr)))
	y_err = list(arrayerr[i][1] for i in range(len(arrayerr)))
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=np.arange(100,N_max), y = y_coord , mode = 'markers', error_y = dict(type = 'data' , array = y_err , color = 'purple', thickness = 1.5, width = 3), marker = dict(color = 'green', size = 8)))
	fig.show()
	
   	


if __name__ == "__main__":
    main()
