import sys
import random
import matplotlib.pyplot as plt
import numpy as np
import math

'''def controllo_decimale(n) :
	if n > 0:
    	digits = int(math.log10(n)) + 1
	elif n == 0:
    	digits = 1
	elif n < 0:
    	digits = int(math.log10(-n)) + 2
	return digits '''

def exp_pdf(x, tau):
    if tau <= 0:
        raise ValueError("τ deve essere maggiore di 0.")
    return np.exp(-x / tau) / tau


def likelihood(theta, pdf, lista):
    r = 1
    if len(lista)>100 :
    	lista2 = lista[:100]
    	for x in lista2:
    		r*= pdf(x, theta)
    else :
    	for x in lista:
    		r *= pdf(x, theta)
    return r


def loglikelihood(theta, pdf, lista):
    r = 0
    for x in lista:
        pdf_val = pdf(x, theta)
        if pdf_val > 0:
            r += np.log(pdf_val)
    return r


def sturges(x):
    return int(np.ceil(1 + 3.322 * np.log(x)))


def inv_exp(y, lamb):
    return -np.log(1 - y) / lamb


def rand_exp(tau):
    lamb = 1 / tau
    return inv_exp(random.random(), lamb)


def exp_distribution(tau, N, seed=0):
    if seed != 0:
        random.seed(seed)

    return [rand_exp(tau) for _ in range(N)]


def main():
    # Controllo degli argomenti
    if len(sys.argv) < 3:
        print("Uso: python script.py <N> <tau>")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        tau = float(sys.argv[2])
    except ValueError:
        print("Errore: assicurati che N sia un intero e τ sia un float.")
        sys.exit(1)

    # Genera una lista di numeri casuali con distribuzione esponenziale
    randlist = exp_distribution(tau, N)

    # Calcola la likelihood per una gamma di valori di τ
    taus = np.linspace(0.1, 5, 200)
    lks = [likelihood(ta, exp_pdf, randlist) for ta in taus]

    # Calcolo del numero di bin dell'istogramma
    Nbins = sturges(len(randlist))
    bin_edges = np.linspace(0., max(randlist), Nbins)
    x = np.linspace(0, max(randlist) + 1, 1000)

    # Istogramma dei numeri casuali
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, exp_pdf(x, tau), color='green', lw=3, label='exponential pdf')
    ax.set_title('Histogram of random numbers', size=14)
    ax.set_xlabel('random value')
    ax.set_ylabel('density')
    ax.hist(randlist, bins=bin_edges, color='orange', density=True, alpha=0.7)
    ax.set_xlim(0, max(randlist) + 1)
    ax.legend()

    plt.show()

    # Grafico della likelihood
    fig, ax = plt.subplots(1, 1)
    ax.set_title('Likelihood al variare di τ', size=14)
    ax.set_xlabel('τ')
    ax.set_ylabel('Likelihood')
    ax.plot(taus, lks, color='green', lw=2, label="Likelihood")
    ax.legend()
    ax.set_xlim(taus[0], taus[-1])

    plt.show()


if __name__ == "__main__":
    main()
