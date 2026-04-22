import numpy as np 
import random 
import time 

def factorial(x) :
	if x == 1 :
		return 1 
	else :
		return x*factorial(x-1)
		
		
def main() :
	print(factorial(5))



if __name__ == '__main__' :
	main()
	
