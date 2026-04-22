import sys
import math

def soluzioneq2(a,b,c) :
	if b**2 -4*a*c < 0 :
		print("L'equazione di secondo grado non ha soluzioni")
		return False
	else :
		x1=(-b+math.sqrt(b**2 -4*a*c))/2*a
		x2=(-b-math.sqrt(b**2 -4*a*c))/2*a
		return x1,x2


def main() :
	a = float(input("Inserisci il coefficiente di x^2:\n"))
	b = float(input("Inserisci il coefficiente di x:\n"))
	c = float(input("Inserisci il coefficiente di termine noto:\n"))
	if soluzioneq2(a,b,c) != False :
		sol1, sol2 = soluzioneq2(a,b,c)
		print("La prima soluzione:", sol1 ,"\t","La seconda soluzione:" ,sol2 , "\n")


if __name__ == "__main__" :
	main()
