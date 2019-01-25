import os
#Création dossier "Collaboration" et sous dossier
def creer_dossier(dossier, sousdossiers):
	for rep in sousdossiers:
		os.makedirs(dossier+ '/' +rep)
#Création fichiers textes dans chaque sous dossier
	fdev = open("./Collaboration/developpements/developpements.txt", "w")
	fdev.write ("Ce répertoire contiendra vos développements")
	fdev.close()
	ftest = open("./Collaboration/tests/tests.txt", "w")
	ftest.write ("Ce répertoire contiendra vos tests")
	ftest.close()
	fliv = open("./Collaboration/livraisons/livraisons.txt", "w")
	fliv.write("Ce répertoire contiendra vos livraisons")
	fliv.close()
	fbug = open("./Collaboration/bugs/bugs.txt", "w")
	fbug.write("Ce répertoire contiendra les bugs rencontrés")
	fbug.close()

	print("Dossier et fichiers textes créés")