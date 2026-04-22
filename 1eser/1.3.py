import sys 

def fibonacci(n) :       #def main(): print("Hello World!") if __name__ == "__main__": main()

	lista = [0,1]
	fib = 0
	fib_lista = [0]
	i = 0
	while i < n :
		print(lista)
		a = lista[0]+lista[1]
		lista[0]= a
		lista.sort()
		fib = lista[0]
		fib_lista.append(fib)
		i +=1
	return fib_lista
		
		
def main() :
	n = int(input("Inserisci il numero fino alla quale vuoi calcolare la serie di Fibonaccci \n:"))
	print(fibonacci(n))	
	
if __name__ == "__main__" :
	main()

		
