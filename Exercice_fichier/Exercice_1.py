'''
Lire les 1000 premiers nombres premiers dans le fichier « exo1.txt » et les ranger dans une
liste. Ecrire dans un nouveau fichier le contenu de cette liste en écrivant 10 nombres par
ligne séparés par un espace chacun.
'''

a = open('TP_fichiers_1_1/exo1.txt', 'r')
content = a.readlines()
a.close()

fr = open('TP_fichiers_1_1/result.txt', 'w')
i = 1
for e in content:
    fr.write(e.replace("\n"," "))
    if i % 10 == 0:
        fr.write('\n')
    i+=1
fr.close()