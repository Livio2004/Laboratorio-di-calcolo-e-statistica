import sys
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson
from numba import jit
import libreria as liv

def sturges(x):
    return int(np.ceil(1 + 3.322 * np.log(x)))

def inv_exp(y, lamb=5):
    return -1 * np.log(1 - y) * lamb

@jit
def compute_poisson_data(means, n_experiments):
    poiss = []
    for mean in means:
        uniform_samples = np.random.uniform(0, 1, (n_experiments, 1000))
        for i in range(n_experiments):
            expo = np.cumsum(-1 * np.log(1 - uniform_samples[i, :]) *5)
            p = np.argmax(expo >= int(5 * mean))
            if expo[p] < int(5 * mean):
                p = len(expo)
            poiss.append(p)  # Corretto append senza slicing
    return poiss

def main():
    n_experiments = 1000
    if len(sys.argv) < 2:
        raise ValueError('Inserisci la media per la distribuzione esponenziale')
    media = float(sys.argv[1])
    if len(sys.argv) > 2:
        raise ValueError('Inserisci solo la media come argomento')

    counts = []
    uniform_samples = np.random.uniform(0, 1, (n_experiments, 1000))
    for i in range(n_experiments):
        expo = np.cumsum(inv_exp(uniform_samples[i, :]))
        p = np.argmax(expo >= int(5 * media))
        if expo[p] < int(5 * media):
            p = len(expo)
        counts.append(p)

    print("Counts:", counts)
    print("Size of counts:", np.size(counts))
    distr = liv.lavoro(counts)
    distr.dato()

    N_bins = sturges(len(counts))
    bin_edges = np.linspace(np.floor(np.min(counts)), np.ceil(np.max(counts)), N_bins)
    print('Length of bin edges container:', len(bin_edges))

    fig, ax = plt.subplots(nrows=3, ncols=1)
    ax[0].hist(counts, bins=bin_edges, label='Istogramma della distribuzione', color='orange', density=True, histtype='step')
    ax[0].vlines(counts, 0, poisson.pmf(counts, media), label='PMF della Poissoniana', linestyles='-', color='orange', lw=5, alpha = 0.01)
    means = np.linspace(0, 150, 150)
    skewness = []
    for p in means:  
        skewness.append(poisson.stats(p, moments = 's'))
    ax[1].plot(means, skewness, color='blue', lw=2, label='Skewness')
    kurtosis = []
    for p in means:
    	kurtosis.append(poisson.stats(p, moments = 'k'))
    ax[2].plot(means, kurtosis, color='blue', lw=2, label='Kurtosis')
    for a in ax:
        a.set_xlabel('Variable')
        a.set_ylabel('Event counts')
        a.legend()
    plt.show()

if __name__ == "__main__":
    main()
