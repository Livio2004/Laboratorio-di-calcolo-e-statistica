import sys
import random
import numpy as np
import matplotlib.pyplot as plt
from libreria import lavoro


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


def inv_exp(y, lamb):
    return -np.log(1 - y) / lamb


def rand_exp(tau):
    lamb = 1 / tau
    return inv_exp(random.random(), lamb)


def exp_distribution(tau, N, seed=None):

    return np.array([rand_exp(tau) for _ in range(N)])


def max1(f, xmin, xmax, prec=0.0001, max_attempts=10000):
    phi = (np.sqrt(5) - 1) / 2
    x1 = xmin + phi * (xmax - xmin)
    x2 = xmin + (1 - phi) * (xmax - xmin)
    i = 0
    while abs(xmax - xmin) > prec and i < max_attempts:
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


def main():
    if len(sys.argv) < 3:
        print("Uso: python script.py <tau_true> <N>. Usa tau > 2 ")
        return
    tau_true = float(sys.argv[1])
    N = int(sys.argv[2])
    random.seed(42)
    #np.random.seed(42)
    #np.random.exponential(tau_true,N)
    randlist = exp_distribution(tau_true, N)
    #massimo della likelihood
    #a, b = tau_true-1, tau_true +1
    a, b = 4, 5.5
    taus = np.linspace(1,tau_true*2, 1000)
    distr = lavoro(randlist)
    distr.isto()
    	
    log_likelihood_func = lambda theta: loglikelihood(theta, exp_pdf, randlist)
    tau_est, max_likelihood = max1(log_likelihood_func, a, b)
    lks = [log_likelihood_func(tau) for tau in taus]
    
    #zeri e intervallo di confidenza
    threshold = max_likelihood - 1/2
    func = lambda tau : loglikelihood(tau, exp_pdf, randlist) -threshold
    tau_minus = bisezione(1, tau_est, func)
    tau_plus = bisezione(tau_est,tau_true*2,func)
    
    sigma_minus = tau_est -tau_minus
    sigma_plus = tau_plus - tau_est
    print(sigma_minus, sigma_plus)
    sigma_mean = np.mean(randlist)/np.sqrt(len(randlist))
    print(sigma_mean)
        
	#plot of the function
    plt.figure(figsize = (10,6))
    plt.plot(taus, lks, label = 'Log likelihood profile', color = 'blue')
    plt.axhline(threshold, color = 'green' , linestyle = '--', label = ' Threshold (max-1/2)')
    plt.axvline(tau_true, color = 'red', linestyle = '--', label = f"Valore vero di tau = {tau_true}")
    plt.axvline(tau_est, color = 'orange', linestyle = '--', label = f"Tau stimato = {tau_est: .2f}")
    plt.axvline(tau_minus, color = 'purple', linestyle = '--', label =f"sigma - = {tau_minus:.3f}")
    plt.axvline(tau_plus, color = 'purple', linestyle = '--', label = f"sigma + = {tau_plus:.3f}")
    
    plt.fill_betweenx([threshold, max_likelihood], tau_minus, tau_plus, color = 'purple' ,label = 'Intervallo di confidenza', alpha = 0.4)
    
    plt.title('loglikelihood e intervallo di confidenza')
    plt.xlabel('tau')
    plt.ylabel('loglikelihood')
    plt.xlim(tau_true-1/2,tau_true+1/2)
    plt.ylim(threshold-1, max_likelihood +1)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
