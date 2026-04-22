import sys



a = float(input("Inserisci il primo lato:\n"))
b = float(input("Inserisci il secondo lato: \n"))
c = float(input("Inserisci il terzo lato:\n"))

triangolo = [a,b,c]

triangolo.sort()

if((triangolo[0]**2 + triangolo[1]**2) == triangolo[2]**2):
	print("Il triangolo dato è rettangolo")
elif((triangolo[0]**2 + triangolo[1]**2) > triangolo[2]**2):
	print("Il triangolo è acutangolo")
else :
	print("Il triangolo è ottusangolo")
	
	



