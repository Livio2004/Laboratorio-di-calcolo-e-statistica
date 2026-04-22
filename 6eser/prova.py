import numpy as np
import matplotlib.pyplot as plt

def bisection(xmin, xmax, f, prec=0.0001, max_attempts=100000):
    if f(xmin) * f(xmax) >= 0:
        raise ValueError("No zero in the interval or function has the same sign at interval endpoints.")
    
    i = 0
    while i < max_attempts and (xmax - xmin) > prec:
        xave = (xmin + xmax) / 2
        if f(xave) == 0:
            return xave
        elif f(xmin) * f(xave) > 0:
            xmin = xave
        else:
            xmax = xave
        i += 1
    return xave  # return midpoint as root approximation

def golden_section_search(f, a, b, tol=0.0001):
    phi = (1 + np.sqrt(5)) / 2
    resphi = 2 - phi
    x1 = a + resphi * (b - a)
    x2 = b - resphi * (b - a)
    while abs(b - a) > tol:
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = a + resphi * (b - a)
        else:
            a = x1
            x1 = x2
            x2 = b - resphi * (b - a)
    return (a + b) / 2  # return midpoint as minimum approximation

# Example function
def example_function(x):
    return x**2 - 4

def main():
    # Define interval and function
    xmin, xmax = -3, 3
    x_values = np.linspace(xmin, xmax, 500)
    y_values = example_function(x_values)

    # Use bisection method
    root = bisection(-3, 0, example_function)
    print("Root found by bisection method:", root)

    # Use golden section search method on positive interval for the minimum
    min_x = golden_section_search(example_function, 0, 3)
    print("Minimum found by golden section method:", min_x)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label="f(x) = x^2 - 4", color="blue")
    plt.axhline(0, color='gray', linestyle='--')

    # Plot root found by bisection method
    plt.plot(root, example_function(root), 'ro', label="Bisection root")
    
    # Plot minimum found by golden section method
    plt.plot(min_x, example_function(min_x), 'go', label="Golden section minimum")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Function Plot with Bisection and Golden Section Points")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
