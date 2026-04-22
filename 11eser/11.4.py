from iminuit import Minuit 
from iminuit.cost import LeastSquares
import matplotlib.pyplot as plt
import numpy as np

def f(x,a,b,c) :
	return a*x**2 + b*x + c

	
	

def main():
	
	a = 1
	b = 2
	c = 1.5
	err_epsilon = 0.5
	epsilon = np.random.normal(0, err_epsilon, size = 10)
	x_coord = np.arange(0,10,1)
	y_coord = np.zeros(10)
	for i in range(10) :
		y_coord[i] = f(x_coord[i], a, b,c) + epsilon[i]
	sigma_y = err_epsilon*np.ones(len(epsilon))
	least_squares = LeastSquares(x_coord, y_coord, sigma_y, f)
	fit = Minuit(least_squares, a=0, b=0, c = 0)
	fit.migrad()
	fit.hesse()
	Q_squared = fit.fval
	N_dof = fit.ndof
	print('success of the fit:' , fit.valid)
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
	
	
		
		
	
	
	
	
	
if __name__ == '__main__' :
	main()
