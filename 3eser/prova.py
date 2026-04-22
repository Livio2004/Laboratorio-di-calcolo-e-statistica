import numpy as np
import sys 


def main() :
	with open('sample.txt', 'r') as input_file :
		sample = [int(x) for x in input_file.readlines()]
	print(sample)
	print(np.loadtxt('sample.txt'))
			
if __name__ == "__main__":
	main ()
		
