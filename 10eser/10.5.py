import sys
import random
import numpy as np
import matplotlib.pyplot as plt


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
    if len(sys.argv) < 2:
        print("Uso: python script.py <tau_true>. Usa tau > 2")
        return

    tau_true = float(sys.argv[1])
    sample_size = [100, 300, 500, 1000]
    taus = np.linspace(1, 10, 500)
    plt.figure(figsize = (10,6))
    colors = plt.cm.viridis(np.linspace(0,1, len(sample_size)))
    for n, color in zip(sample_size, colors) :
        randlist = exp_distribution(tau_true, n)
        loglikelihood_func = lambda theta: loglikelihood(theta, exp_pdf, randlist)
        a, b = 1, tau_true * 2
        tau_est, _ = max1(loglikelihood_func, a, b)
        lks = [loglikelihood(tau, exp_pdf, randlist) for tau in taus]
        max_loglikelihood = np.max(lks)
        loglikelihood_ratios = lks - max_loglikelihood
        plt.plot(taus, loglikelihood_ratios, label = f"Sample size = {n}")
        plt.axvline(tau_est, color = color, linestyle = '--', label = f" Tau stimata = {tau_est}")

    plt.title('Loglikelihood ratio vs parametro tau', fontsize = 14)
    plt.xlabel('tau', fontsize = 12)
    plt.ylabel('log likelihood normalizzta')
    plt.axvline(tau_true, label = f"True tau = {tau_true}")
    plt.axhline(np.log(1/2))
    plt.legend()
    plt.grid(True)
    plt.show()
	

if __name__ == "__main__":
    main()
