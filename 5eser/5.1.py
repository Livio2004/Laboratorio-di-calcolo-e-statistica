
import sys
import random
import matplotlib.pyplot as plt
import numpy as np
from math import gcd


def inv_exp (y, lamb = 1) :
   
    return -1 * np.log (1-y) / lamb


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

class Fraction :
	
	def __init__(self, numerator, denominator) :
		
		if denominator == 0 :
			raise ValueError('Il denominatore non può essere 0')
		
		if type(numerator) != int  :
			raise TypeError('Il numeratore deve essere di tipo int')
		
		if type(denominator) != int :
			raise TypeError('Il denominatore deve essere di tipo int')
			
		gcd1 = int(np.gcd(numerator, denominator))
		
		self.numerator = numerator // gcd1
		self.denominator = denominator // gcd1
		print(type(self.numerator))
		
	def stampa(self) :
		print(self.numerator, '/' , self.denominator)
		
		
	def __add__(self, fraction) : #overloading della somma, sottrazione...
		new_numerator = self.numerator * fraction.denominator + fraction.numerator * self.denominator
		new_denominator = self.denominator * fraction.denominator
		return Fraction (new_numerator, new_denominator) 
		
	def __sub__(self, fraction) :
		new_numerator = self.numerator * fraction.denominator - fraction.numerator * self.denominator
		new_denominator = self.denominator * fraction.denominator
		return Fraction (new_numerator, new_denominator)
		
	def __mul__(self, fraction) :
		new_numerator = self.numerator * fraction.numerator 
		new_denominator = self.denominator * fraction.denominator 
		return Fraction(new_numerator, new_denominator)
		
	def __truediv__(self, fraction) :
		new_numerator = self.numerator * fraction.denominator 
		new_denominator = self.denominator * fraction.numerator  
		return Fraction(new_numerator, new_denominator)
		
def testing() :
	frazione_iniziale = Fraction (1,2) 
	frazione_iniziale.stampa()
	frazione2 = Fraction(1,4) 
	frazione2.stampa()
		
	sum1 = frazione_iniziale + frazione2
	sum1.stampa()
	sub1 = frazione_iniziale -frazione2
	sub1.stampa()
	mul1 = frazione_iniziale * frazione2
	mul1.stampa()
	div1 = frazione_iniziale/frazione2
	div1.stampa()
		
		
def main() :
	testing ()
		
		
		
		
if __name__ == "__main__" :
    main()
		
	
		
		
			
			
	
		
		
