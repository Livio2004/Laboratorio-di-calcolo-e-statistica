import numpy as np
import matplotlib.pyplot as plt

# Log-likelihood function
def log_likelihood(tau, data):
    if tau <= 0:
        return -np.inf
    return -len(data) * np.log(tau) - np.sum(data) / tau
    
# Dynamic interval adjustment
def find_bracketing_interval(func, initial_a, initial_b, step=0.1, max_iterations=100):
    """Dynamically find an interval [a, b] where func(a) and func(b) have opposite signs."""
    a, b = initial_a, initial_b
    for _ in range(max_iterations):
        if func(a) * func(b) < 0:
            return a, b
        if abs(func(a)) < abs(func(b)):
            a -= step  # Expand interval on the left
        else:
            b += step  # Expand interval on the right
    raise ValueError("Failed to find a bracketing interval.")

# Bisection method to find τ ± στ
def bisection(func, a, b, tol=1e-5, max_iter=100):
    fa, fb = func(a), func(b)
    if fa * fb > 0:
        raise ValueError("Function does not change sign in the interval.")
    iter_count = 0
    while abs(b - a) > tol and iter_count < max_iter:
        c = (a + b) / 2
        fc = func(c)
        if fa * fc < 0:
            b = c
        else:
            a = c
        iter_count += 1
    return (a + b) / 2

# Parameters
np.random.seed(42)
tau_true = 5.0
num_toy_experiments = 1000
event_counts = [10, 50, 100, 500, 1000]

# Results storage
means = []
stds = []

for n in event_counts:
    differences = []

    for _ in range(num_toy_experiments):
        # Generate data
        data = np.random.exponential(scale=tau_true, size=n)

        # Estimate τ and find confidence interval
        taus = np.linspace(1, 10, 500)
        log_likelihood_values = [log_likelihood(tau, data) for tau in taus]
        tau_est = taus[np.argmax(log_likelihood_values)]
        max_log_likelihood = max(log_likelihood_values)

        # Find στ using bisection with dynamic interval adjustment
        threshold = max_log_likelihood - 0.5
        func = lambda tau: log_likelihood(tau, data) - threshold
        a_left, b_left = find_bracketing_interval(func, tau_est - 1, tau_est)
        tau_minus = bisection(func, a_left, b_left)
        a_right, b_right = find_bracketing_interval(func, tau_est, tau_est + 1)
        tau_plus = bisection(func, a_right, b_right)
        sigma_tau = (tau_plus - tau_minus) / 2

        # Calculate normalized difference
        difference = (tau_est - tau_true) / sigma_tau
        differences.append(difference)

    # Compute mean and standard deviation of differences
    means.append(np.mean(differences))
    stds.append(np.std(differences))

    # Plot histogram for the current number of events
    plt.figure(figsize=(8, 4))
    plt.hist(differences, bins=30, density=True, alpha=0.7, color="blue", label="Histogram")
    plt.title(f"Distribution of Normalized Differences (n={n})")
    plt.xlabel("Normalized Difference: $(\\tau - \\tau_{true}) / \\sigma_\\tau$")
    plt.ylabel("Density")
    plt.axvline(0, color="red", linestyle="--", label="Expected Mean (0)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot mean and standard deviation as a function of event counts
plt.figure(figsize=(10, 6))
plt.plot(event_counts, means, marker="o", label="Mean of Differences")
plt.plot(event_counts, stds, marker="s", label="Standard Deviation of Differences")
plt.axhline(0, color="red", linestyle="--", label="Expected Mean (0)")
plt.axhline(1, color="green", linestyle="--", label="Expected Std (1)")
plt.title("Mean and Std of Normalized Differences vs Number of Events")
plt.xlabel("Number of Events")
plt.ylabel("Parameter Value")
plt.legend()
plt.grid(True)
plt.show()
