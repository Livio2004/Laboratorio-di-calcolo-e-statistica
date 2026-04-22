import sys 
import numpy as np 
import math 
import matplotlib.pyplot as plt
import time as tm
def percentage25(array, N):
	array = np.sort(array)
	result = array[int(N/4)]
	return result
	
def percentage75(array, N):
	array = np.sort(array)
	result = array[int((3*N)/4)]
	return result
	
def percentage(array, N, cent) :
	array = np.sort(array)
	result = array[int((cent/100)*N)]
	return result
