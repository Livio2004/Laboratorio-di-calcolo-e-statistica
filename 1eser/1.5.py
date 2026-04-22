import sys 
def even_odd(n) :
	if n%2 == 0:
		return True
	else :
		return False
		

def fibonacci(n) :       #def main(): print("Hello World!") if __name__ == "__main__": main()

	lista = [0,1]
	fib = 0
	fib_lista = [0]
	i = 0
	while i < n :
		a = lista[0]+lista[1]
		lista[0]= a
		lista.sort()
		fib = lista[0]
		fib_lista.append(fib)
		i +=1
	return fib_lista
		
		
def main() :
	lista_pari =  []
	lista_dispari = []
	n = int(input("Inserisci il numero fino alla quale vuoi calcolare la serie di Fibonaccci \n:"))
	lista_totale = fibonacci(n)
	print(lista_totale)
	i = 0
	for i in range(n+1) :
		if even_odd(i) == True :
			lista_pari.append(lista_totale[i])
		else :
			lista_dispari.append(lista_totale[i])
	print(lista_pari)
	print(lista_dispari)
			

if __name__ == "__main__" :
	main()
