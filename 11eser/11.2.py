from iminuit import Minuit 
from iminuit.cost import LeastSquares
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

def f(x,m,q) :
	return m*x + q

	
def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))

def main():
	
	m_true = 1.5
	q_true = 1
	err_epsilon = 0.5
	N_toys = 10000
	Q_results = []
	ndof = 0
	for _ in range(N_toys) :
		epsilon = np.random.normal(0, err_epsilon, size = 10)
		x_coord = np.arange(0,10,1)
		y_coord = np.zeros(10)
		for i in range(10) :
			y_coord[i] = f(x_coord[i], m_true, q_true) + epsilon[i]
		sigma_y = err_epsilon*np.ones(len(epsilon))
		least_squares = LeastSquares(x_coord, y_coord, sigma_y, f)
		fit = Minuit(least_squares, m=0, q=0)
		fit.migrad()
		fit.hesse()
		Q_squared = fit.fval
		Q_results.append(Q_squared)
		ndof = fit.ndof
	plt.figure(figsize=(10, 6))
	N_bins = sturges(len(Q_results))
	bin_edges = np.linspace(np.min(Q_results), np.max(Q_results), N_bins)
	plt.hist(Q_results, bin_edges, label = f'Distribuzione del Q square con {ndof} gradi di libertà', alpha=0.5)
	plt.axvline(ndof, label = 'expected value of Q_squared', color = 'red')
	plt.legend()
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show()
	
	
	
		
		
	
	
	
	
	
if __name__ == '__main__' :
	main()
