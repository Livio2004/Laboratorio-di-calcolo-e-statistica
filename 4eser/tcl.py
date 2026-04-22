import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))

def main() :
	fig, ax = plt.subplots(nrows = 1, ncols = 1)
	n_events = 10000
	n_sum = 12
	uniform_samples = np.random.uniform(0, 1, (n_events, n_sum))
	summed_samples = np.sum(uniform_samples, axis=1)
	gaussian_samples = np.sort((summed_samples - n_sum / 2) / np.sqrt(n_sum / 12))
	N_bins = sturges(len(gaussian_samples))
	bin_edges = np.linspace(np.min(gaussian_samples), np.max(gaussian_samples), N_bins)
	ax.hist(gaussian_samples, bin_edges, color = 'green', lw = 2, label = 'histogram', density = True)

	ax.plot(gaussian_samples, norm.pdf(gaussian_samples, loc = 0, scale = 1), color = 'r', label = 'original pdf' , lw = 2)
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_title('Uniform Distribution')
	plt.legend()
	plt.style.use('seaborn-v0_8')
	plt.show()
	
if __name__ == '__main__' :
	main()
