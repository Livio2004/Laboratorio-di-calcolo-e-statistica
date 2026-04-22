import sys
import random
import numpy as np
import matplotlib.pyplot as plt
from numba import njit 

def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))
	
def exp_pdf(x, tau):
    if tau <= 0:
        raise ValueError("τ deve essere maggiore di 0.")
    return np.exp(-x / tau) / tau

def loglikelihood(theta, pdf, lista):
    r = 0
    for x in lista:
        pdf_val = pdf(x, theta)
        if pdf_val > 0:
            r += np.log(pdf_val)
    return r

@njit
def inv_exp(y, lamb):
    return -np.log(1 - y) / lamb

@njit
def rand_exp(tau):
    lamb = 1 / tau
    return inv_exp(np.random.random(), lamb)

@njit
def exp_distribution(tau, N):
    result = np.empty(N)
    for i in range(N):
        result[i] = rand_exp(tau)
    return result

def max1(f, xmin, xmax, prec=0.01, max_attempts=10000):
    phi = (np.sqrt(5) - 1) / 2
    x1 = xmin + phi * (xmax - xmin)
    x2 = xmin + (1 - phi) * (xmax - xmin)
    i = 0
    while np.abs(xmax - xmin) > prec and i < max_attempts:
        if f(x2) < f(x1):
            xmin = x2
            x2 = x1
            x1 = phi * (xmax - xmin) + xmin
        else:
            xmax = x1
            x1 = x2
            x2 = xmin + (1 - phi) * (xmax - xmin)
        i += 1
    x_max = (x1 + x2) / 2
    return x_max, f(x_max)
  
def bisezione(xmin, xmax, f, prec = 0.01 , max_attempts = 10000) : #uso un numero massimo di attempt come check
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


def main():
    if len(sys.argv) < 3:
        print("Uso: python script.py <tau_true> <N>. Usa tau > 2 ")
        return
    random.seed(20)
    tau_true = float(sys.argv[1])
    N_toys = 100
    N_events = int(sys.argv[2])
    taus = np.linspace(1,tau_true*2,1000)
    a, b = tau_true-1, tau_true +1
    tau = []
    
    #np.random.seed(42)
    #np.random.exponential(tau_true,N)
    for _ in range(N_toys) :
    	randlist = exp_distribution(tau_true, N_events)
    	log_likelihood_func = lambda theta: loglikelihood(theta, exp_pdf, randlist)
    	tau_est, _ = max1(log_likelihood_func, a, b)
    	tau.append(tau_est)
    
    randlist = exp_distribution(tau_true, N_events)	
    log_likelihood_func = lambda theta: loglikelihood(theta, exp_pdf, randlist)
    tau_est, max_likelihood = max1(log_likelihood_func, a, b)
    
    
    #zeri e intervallo di confidenza
    threshold = max_likelihood - 1/2
    func = lambda tau : loglikelihood(tau, exp_pdf, randlist) -threshold
    sigma_minus = bisezione(1, tau_est, func)
    sigma_plus = bisezione(tau_est,tau_true*2,func)
      
	#plot of the function
    plt.figure(figsize = (10,6))
    N_bins = 30
    bin_edges = np.linspace(np.floor(np.min(tau)),np.ceil(np.max(tau)),N_bins)
    plt.hist(tau, bins = bin_edges, label = 'Istogramma della distribuzione', color = 'orange', density = True)
    plt.axvline(tau_true, color = 'red', linestyle = '--', label = f"Valore vero di tau = {tau_true}")
    plt.axvline(tau_est, color = 'brown', linestyle = '--', label = f"Tau stimato = {tau_est: .2f}")
    plt.axvline(sigma_minus, color = 'purple', linestyle = '--', label =f"sigma - = {sigma_minus:.3f}")
    plt.axvline(sigma_plus, color = 'purple', linestyle = '--', label = f"sigma + = {sigma_plus:.3f}")
    
    
    plt.title('loglikelihood e intervallo di confidenza')
    plt.xlabel('tau')
    plt.ylabel('loglikelihood')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
