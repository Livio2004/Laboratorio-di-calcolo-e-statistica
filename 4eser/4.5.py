import matplotlib.pyplot as plt
import numpy as np
import sys 
from scipy.stats import norm
import random


def sturges(x):
    return int(np.ceil(1 + 3.322 * np.log(x)))


class GRN:
    def __init__(self, seed=None):
        self.seed(seed)
    
    def seed(self, seed):
        random.seed(seed)
    
    def random(self):
        return random.random()
    
    def rand(self, xmin, xmax):
        return xmin + self.random() * (xmax - xmin)


def TAC(xmin, xmax, ymax, my_GRN, f, max_attempts=100000):
    attempts = 0
    while attempts < max_attempts:
        x = my_GRN.rand(xmin, xmax)
        y = my_GRN.rand(0, ymax)
        if y <= f(x):
            return x
        attempts += 1
    print('Maximum attempts reach')
    return None

def main():
    if len(sys.argv) != 4:
        print('Usage: python script.py xmin xmax ymax')
        sys.exit()

    try:
        xmin = float(sys.argv[1])
        xmax = float(sys.argv[2])
        ymax = float(sys.argv[3])
    except ValueError:
        print('xmin, xmax, and ymax must be numbers')
        sys.exit()

    items = int(input('Enter the number of random numbers you want: '))
    seed = float(input('Enter the seed value: '))

    my_GRN = GRN(seed)
    sample = []
    
    for _ in range(items):
        sample_value = TAC(xmin, xmax, ymax, my_GRN, lambda x : norm.pdf(x, loc = 0, scale = 1))
        if sample_value is not None:
            sample.append(sample_value)
        else:
            print("Sample could not be generated. Check ymax or range of the PDF")

  
    N_bins = sturges(len(sample))
    bin_edges = np.linspace(np.min(sample), np.max(sample), N_bins)

  
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.hist(sample, bin_edges, color='red', label='Generated Distribution', density=True)
    

    x_values = np.linspace(xmin, xmax, 1000)
    ax.plot(x_values, norm.pdf(x_values, loc=0, scale=1), 'b-', lw=2, label='Normal PDF')
    
    ax.set_xlabel('Values')
    ax.set_ylabel('Density')
    ax.legend()
    plt.style.use("seaborn-v0_8")
    plt.show()

if __name__ == "__main__":
    main()
