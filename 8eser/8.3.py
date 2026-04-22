import sys
import random
import matplotlib.pyplot as plt
import numpy as np
from numba import jit
import libreria as liv


def main():
    N_toys = 10000
    if len(sys.argv) > 2:
        raise ValueError('Inserisci il numero massimo dei 100 esperimenti')
    N_max = int(sys.argv[1])


    uniform_samples = np.random.uniform(0, 100, (N_toys, N_max))
    means = []
    err_media = []
    for i in range(N_toys) :
    	distribuzione = liv.lavoro(uniform_samples[i, :])
    	means.append(distribuzione.media())
    	err_media.append(distribuzione.errore_standard())
    print(np.mean(err_media))
    finald = liv.lavoro(means)
    finald.dato()
    finald.isto()

if __name__ == "__main__":
    main()
