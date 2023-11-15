
def rankTeams(names, lostTo):

	a=""
	b=""


	for h in range(len(names)):
		for i in range(len(names)):
			for k in range(len(lostTo)):
				if (i==0):
					pass
				if(names[i]==""):
					pass
				if (names[i]==lostTo[k]):
					print("====", i,k)
					print(names)
					print(lostTo)
					a=names[i]
					b=names[i-1]
					names[i] = b
					a=names[i-1]

					a=lostTo[k]
					b=lostTo[k-1]
					lostTo[k] = b
					a=lostTo[k-1]
					print(names)
					print(lostTo)
	print(names)

lista1 = ["EQUIPO1","EQUIPO2","EQUIPO3","EQUIPO4"]
lista2 = ["EQUIPO2","EQUIPO4","EQUIPO4",""]
rankTeams(lista1, lista2)