from iminuit import Minuit 
from iminuit.cost import LeastSquares
import matplotlib.pyplot as plt
import numpy as np

def f(x,m,q) :
	return m*x + q
	
def cov(x,y,sy) :
  t = -1*(np.sum(x)/(len(x)*np.sum(x**2)-(np.sum(x))**2))
  r = t*(np.power(sy,2))
  return r

	
	

def main():
	
	m_true = 1.5
	q_true = 1
	err_epsilon = 0.5
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
	N_dof = fit.ndof
	print('success of the fit:' , fit.valid)
	my_Q = np.sum(np.power((y_coord-f(x_coord, *fit.values))/sigma_y,2))
	print(type(my_Q))
	print('differenza tra i due Q_values:', my_Q -Q_squared)
	print(fit.covariance)
	
	
	plt.errorbar(x_coord, y_coord, sigma_y, fmt="ok", label="data")
	plt.plot(x_coord, f(x_coord, *fit.values), label="fit")
	
	fit_info = [
    f"$\\chi^2$/$n_\\mathrm{{dof}}$ = {fit.fval:.1f} / {fit.ndof:.0f} = {fit.fmin.reduced_chi2:.1f}",
]
	for p, v, e in zip(fit.parameters, fit.values, fit.errors):
		fit_info.append(f"{p} = ${v:.3f} \\pm {e:.3f}$")

	plt.legend(title="\n".join(fit_info), frameon=False)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show()
	
	plt.figure(figsize = (10,6))
	x_coord2 = np.linspace(0,10,1000)
	y_coord2 = np.zeros(len(x_coord2))
	m = fit.values[0]
	q = fit.values[1]
	for i in range(len(x_coord2)) :
		y_coord2[i] = f(x_coord2[i], m, q) 	
	
	sigmay = np.sqrt(np.power(fit.errors[0],2)+np.power(fit.errors[1],2)+2*fit.covariance[0][1])*np.ones(len(x_coord2))
	
	plt.plot(x_coord2, f(x_coord2,*fit.values)+sigmay, color = 'red')
	plt.plot(x_coord2, f(x_coord2, *fit.values), label="estrapolazione")
	plt.plot(x_coord2, f(x_coord2, *fit.values)-sigmay, color = 'blue')
	
	plt.show()
	
	
	
	
	
	
		
		
	
	
	
	
	
if __name__ == '__main__' :
	main()
