import sys
import random
import matplotlib.pyplot as plt
import numpy as np


def exp_pdf(x, tau):
    if tau <= 0:
        raise ValueError("τ deve essere maggiore di 0.")
    return np.exp(-x / tau) / tau


def likelihood(theta, pdf, lista):
    r = 1
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

    lista = [rand_exp(tau) for _ in range(N)]
    return lista




def main():
    N = int(sys.argv[1])
    tau = float(sys.argv[2])
    taus = np.linspace(0.1, 5, 200)
    randlist = exp_distribution(tau, N)
    
    lks = []
    for ta in taus:
        lks.append(loglikelihood(ta, exp_pdf, randlist))
    
    # Grafico della log-likelihood
    fig, ax = plt.subplots(1, 1)
    ax.set_title('Log-Likelihood al variare di τ', size=14)
    ax.set_xlabel('τ')
    ax.set_ylabel('Log-Likelihood')
    ax.plot(taus, lks, color='green', lw=2, label="Log-Likelihood")
    ax.legend()

    plt.show()

if __name__ == "__main__":
	main ()
