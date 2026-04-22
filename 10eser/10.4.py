import sys
import random
import numpy as np
import matplotlib.pyplot as plt


def exp_pdf(x, tau):
    if tau <= 0:
        raise ValueError("τ deve essere maggiore di 0.")
    return np.exp(-x / tau) / tau


def loglikelihood(theta, pdf, lista):
   	result = likelihood(theta,pdf,lista)
   	return np.log(result)
   	

def likelihood(theta, pdf, lista):
    r = 1
    for x in lista:
    	r *= pdf(x, theta)
    return r

def inv_exp(y, lamb):
    return -np.log(1 - y) / lamb


def rand_exp(tau):
    lamb = 1 / tau
    return inv_exp(random.random(), lamb)


def exp_distribution(tau, N, seed=None):
    if seed is not None:
        random.seed(seed)

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


def main():
    if len(sys.argv) < 3:
        print("Uso: python script.py <tau_true> <N>. Usa tau > 2")
        return

    tau_true = float(sys.argv[1])
    N = int(sys.argv[2])
    randlist = exp_distribution(tau_true, N, seed=42)
    a_initial, b_initial = 1, tau_true * 2

    log_likelihood_func = lambda theta: loglikelihood(theta, exp_pdf, randlist)
    tau_est, max_likelihood = max1(log_likelihood_func, a_initial, b_initial)

    tau_mean = np.mean(randlist)
    
    
    print(f"True value of tau: {tau_true}")
    print(f"Stima di tau (con max likelihood): {tau_est}")
    print(f"Stima con la media: {tau_mean}")

    intervals = [(1, tau_true), (1, tau_true + 2), (2, tau_true + 2), (1, tau_true * 2)]
    results = []

    for a, b in intervals:
        tau_est, _ = max1(log_likelihood_func, a, b)
        results.append((a, b, tau_est))

    print("\nDipendenza dall'intervallo:")
    for a, b, tau_est in results:
        print(f"Intervallo [{a}, {b}]: tau = {tau_est}")
        
	#plot of the function
    fig,ax = plt.subplots(1,1)
    theta = np.linspace(1, tau_true*2, 1000)
    lks = []
   
    for i in theta :
	    result = log_likelihood_func(i)
	    lks.append(result)
		
		
    ax.plot(theta, lks , color = 'red', lw=2, label = 'loglikelihood rispetto a tau')
    ax.axhline(max_likelihood, linestyle = '--')
    ax.scatter(tau_est, max_likelihood, lw = 4, marker = 'o', label = 'massimo con golden aurea')
    ax.set_xlabel('tau')
    ax.set_ylabel('loglikelihood')
    ax.legend()
    plt.show()
	

if __name__ == "__main__":
    main()
