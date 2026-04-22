import sys 
import numpy as np 
import math 
import matplotlib.pyplot as plt
import time as tm

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

def display_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1, r2, mandelbrot_array = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(mandelbrot_array, extent=(ymax, xmax, ymin, xmin), cmap='hot')
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.show()

# Parameters
def main() :
	xmin, xmax = -2.0, 1.0
	ymin, ymax = -1.5, 1.5
	width, height = 1000, 1000
	max_iter = 100

	# Display the Mandelbrot set
	display_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
	print(mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter))
	



if __name__ == "__main__":
  main ()
