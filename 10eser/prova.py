import numpy as np
import matplotlib.pyplot as plt

# Log-likelihood function
def log_likelihood(tau, data):
    if tau <= 0:
        return -np.inf
    return -len(data) * np.log(tau) - np.sum(data) / tau

# Bisection method to find τ ± στ
def bisection(func, a, b, tol=1e-5, max_iter=100):
    """Finds the root of func(x) = 0 in the interval [a, b]."""
    fa, fb = func(a), func(b)
    if fa * fb > 0:
        raise ValueError("Function does not change sign in the interval.")

    iter_count = 0
    while abs(b - a) > tol and iter_count < max_iter:
        c = (a + b) / 2
        fc = func(c)
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        iter_count += 1
    return (a + b) / 2

# Generate exponential data
np.random.seed(42)
tau_true = 5.0
data = np.random.exponential(scale=tau_true, size=1000)

# Find the maximum log-likelihood
taus = np.linspace(1, 10, 1000)
log_likelihood_values = [log_likelihood(tau, data) for tau in taus]
tau_est = taus[np.argmax(log_likelihood_values)]
max_log_likelihood = max(log_likelihood_values)

# Confidence interval: Find τ - στ and τ + στ
threshold = max_log_likelihood - 0.5
func = lambda tau: log_likelihood(tau, data) - threshold
tau_minus = bisection(func, 1, tau_est)
tau_plus = bisection(func, tau_est, 10)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(taus, log_likelihood_values, label="Log-Likelihood Profile", color="blue")
plt.axhline(threshold, color="green", linestyle="--", label="Threshold (Max - 0.5)")
plt.axvline(tau_true, color="red", linestyle="--", label=f"True τ = {tau_true}")
plt.axvline(tau_est, color="orange", linestyle="--", label=f"Estimated τ = {tau_est:.2f}")
plt.axvline(tau_minus, color="purple", linestyle="--", label=f"τ - στ = {tau_minus:.2f}")
plt.axvline(tau_plus, color="purple", linestyle="--", label=f"τ + στ = {tau_plus:.2f}")

# Highlight confidence interval
plt.fill_betweenx(
    [threshold, max_log_likelihood],
    tau_minus,
    tau_plus,
    color="purple",
    alpha=0.2,
    label="Confidence Interval"
)

# Graph labels and legend
plt.title("Log-Likelihood Profile with Confidence Interval", fontsize=14)
plt.xlabel("τ", fontsize=12)
plt.ylabel("Log-Likelihood", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
