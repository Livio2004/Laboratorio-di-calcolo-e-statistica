import sys 
import math

def controllo_primi(n) :
	for i in range(2,n) :
		if n%i == 0 :
			return False
	return True 
		


def main() :
	lista_primi = []
	n = 100 
	for i in range(100) :
		if controllo_primi(i) == True :
			lista_primi.append(i) 
	print(lista_primi)
	


if __name__ == "__main__" :
	main()
