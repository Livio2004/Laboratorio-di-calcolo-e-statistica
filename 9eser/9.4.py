import sys
import random
import numpy as np


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
    if seed is not None:
        random.seed(seed)

    return np.array([rand_exp(tau) for _ in range(N)])


def main():
    if len(sys.argv) < 3:
        print("Uso: python script.py <N_max> <tau>")
        return

    N_max = int(sys.argv[1])
    tau = float(sys.argv[2])

    taus = np.linspace(0.1, 5, 200)  # Intervallo dei τ da testare
    n_values = np.arange(50, N_max + 1, 50)  # Intervallo di N

    # Inizializza una matrice per i risultati
    lks = np.zeros((len(taus), len(n_values)))

    # Ciclo sui valori di N
    for j, N in enumerate(n_values):
        # Genera una lista casuale con τ fisso
        randlist = exp_distribution(tau, N, seed=42)
        # Ciclo sui valori di τ
        for i, ta in enumerate(taus):
            # Calcola la log-likelihood
            lk = loglikelihood(ta, exp_pdf, randlist)
            lks[i, j] = lk
        lks[:, j] = lks[:, j] - np.max(lks[:,j])

    # Stampa i risultati 
    print("Log-Likelihood Matrix:")
    print(lks)

    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    for j, N in enumerate(n_values):
        plt.plot(taus, lks[:, j], label=f'N={N}')
    plt.xlabel(r'$\tau$')
    plt.ylabel('Log-Likelihood')
    plt.title('Log-Likelihood vs $\\tau$ per diversi valori di N')
    plt.legend()
    plt.xlim(1.5,2.5)
    plt.ylim(-20,1)
    plt.axhline( np.log(0.5))
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
