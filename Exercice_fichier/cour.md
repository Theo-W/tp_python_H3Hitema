les fichiers
    -> fichier text
        1 _ ouverture de fichier
            `open('chemain, 'mode ouverture')'`
        2 _ ferme le fichier
            `"votre fichier".close()`
        3 _ Ecrire dans le fichiers
            `"votre fichier".write("mon code")`
        4 _ Lire le contenu
            `"mon fichier".read()` => revoye un string contenant l'integralite du fichier
            `"mon fichier".readlines()` => découpes lignes à lignes et nous revoyer un tableau
        5 _ Déplacer le curseur (lecture/ecriture)
            `"mon fichier".seek("decalage(int)", "origin du décalage")`




 type de fichier
    relation: à partir du répertoire courant
    absolu: à partir de la racine du disque
    
 modes d'ouverture
    "w": ecrire seul
         créer le fichier si il n'existe pas
         ! => vide le fichier à l'ouverture
    "r"  ouverture en lecture seul
         ne créer pas de fichier
         le curseur de lecture se place au début
    "a"  ecrire seul
         créer le fichier s'il n'existe pas
         le curseur ce place à la fin

Origin du décalage
    0 : début du fichier
    1 : position actuel du curseur
    2 : fin du fichier
         