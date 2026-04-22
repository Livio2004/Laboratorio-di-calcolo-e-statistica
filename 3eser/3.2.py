import matplotlib.pyplot as plt
import numpy as np
import sys 
def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))
	

def main() :
	with open('eventi_unif.txt', 'r') as input_file :
		sample = [float(x) for x in input_file.readlines()]
	count = 0	
	
	for i in sample :
		if i > 0 :
			if count <10 :
				print(i)
				count += 1
			else :
				break
	
	print('The number of events are:', len(sample))
	print('The minimum number is :', np.min(sample))
	print('The maximum number is :', np.max(sample))
			
			
	
if __name__ == "__main__":
	main ()
