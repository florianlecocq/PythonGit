def nb_elements(liste):
	compte=0
	for mot in liste:
		compte+=1
	return compte

def afficher_la_liste(liste):
	print(liste)

def ajouter_dans_liste(liste, element):
	if not element in liste:
		liste.append(element)

def remplace(liste,element1,element2):
	index=0
	if element1 in liste:
		liste[index]=element2
	else:
		index+=1
def supprime(liste,element):
	liste.remove(element)

def demoliste():
	ma_liste= ["element1","element2","element3"]
	print("la liste contient",nb_elements(ma_liste)," elements")
	afficher_la_liste(ma_liste)
	
	print("jajoute element 4 dans la liste",ajouter_dans_liste(ma_liste,"element4"))
	afficher_la_liste(ma_liste)

	print("je remplace element1 par tutu")
	remplace(ma_liste,"element1","tutu")
	afficher_la_liste(ma_liste)

	print("je suprime tutu de ma liste")
	supprime(ma_liste,"tutu")
	afficher_la_liste(ma_liste)

def creerliste():
	fin=0
	cpt=1
	liste=[]
	while fin == 0:
		message="element n°"+str(cpt)+" de la liste (champ vide=stop) : "
		entree=input(message)
		if entree != "":
			liste.append(entree)
			cpt+=1
		else:
			fin=1
	return liste

def menu():
	retour=0
	liste= []#creerliste()	

	while retour ==0:
		print("---Menu de la mort !---")
		print("1. Crer votre liste : ajouter les elements")
		print("2. Afficher la liste")
		print("3. Ajouter un element en fin de liste")
		print("4. Remplacer un element de la liste par un autre")
		print("5. Supprimer un element de la liste")
		print("6. nombre d'élements dans la liste")
		print("*. Fin")

		choix=input("Votre choix : ")

		if choix=="1":
			print("Crer votre liste : ajouter les elements")
			liste=creerliste()
			print("----")

		elif choix=="2":
			print("2. Afficher la liste")
			if liste ==[]:
				liste= creerliste()	
			else:
				print("la liste contient",nb_elements(liste)," elements")
				afficher_la_liste(liste)

		elif choix=="3":
			print("3. Ajouter un element en fin de liste")
			ajouter_dans_liste()

		elif choix=="4":
			print("Remplacer un element de la liste par un autre")

		elif choix=="5":
			print("Supprimer un element de la liste")

		elif choix=="6":
			nb_elements()
		else:
			print("Aucun choix")
			print("Fin du programme")
			retour = 1
		


menu()
