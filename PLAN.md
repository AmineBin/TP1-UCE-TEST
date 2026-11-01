Amine Binoumar

###Modifier le plan !!

##Plan de test :
Je vais utiliser pytest pour les tests unitaires, je vais utiliser coverage pour mesurer la couverture des tests, ruff pour tester la qualité du code et pdoc3 pour générer une documentation.
Pour l’algo de triangulation j’ai opté pour de Delaunay qui offre une assez bonne complexité pour les tests tout en étant réalisable sans blocage majeur.

Pour tester l’api et autres éléments dépendants de l'extérieur je vais les mock grâce à mocker.

##Tests unitaires :
**Encodage :**
*Le but de ces tests vont être de veiller à ce que la valeur ne soit pas corrompue*

Vérifier que le passe en binaire d’une valeur fonctionne avec des valeurs négatives
Vérifier que le chiffre binaire correspond bien à la valeur en entré
Vérifier que si quand on reverse le binaire pour repasser en base de 10 on a le bon nombre

**Algo :**
*Lors de ces tests on va veiller à ce que les triangles se forment correctement lors de la triangulation et qu’aucune erreur de logique n’apparaisse lors du processus*

Vérifier qu’il ne peut pas y avoir de point dans un cercle
Vérifier que tous les points ont été utilisés
Vérifier que 3 points donnent un triangle et que 4 points donnent 2 triangles
Vérifier que si les y a seulement 3 points allignés on renvoie une erreur

**Code 200 :** 
*Le but va être de vérifier que lors d’une réussite on reçoit le bon code*
 
Vérifier que le triangle a bien été réalisé

**Code 400 :**
*Le but est de détécter si une requête/donnée erronée a été transféré*

Vérifier que si le format binaire ne contient pas 4 octets on renvoie le bon code
Vérifier que si le chiffre binaire ne correspond pas à la valeur en entrée on renvoie le bon code
Vérifier que si la représentation binaire des pointset n’est la même que pour un pointseter on renvoie le bon code
Vérifier que si il est possible d’avoir une autre valeur qu’un nombre on renvoie le bon code
Vérifier que si il y a moins de 3 point on renvoie le bon code

**Code 404 :**
*Le but est de s’assurer que si on demande un élément qui n’existe pas le code 404 est envoyé*

Vérifier que si le point set id n’a pas été trouvé on renvoie le bon code

*Code 500 :**
Le but est d’avoir un code d’erreur en cas de problème dans le programme

Vérifier que si le code a une erreur on renvoie le bon code

**Code 503 :**
Le but est de vérifier qu’il n’y a aucun soucis de communication avec les éléments exterieur

Vérifier que si la base de donnée est inaccessible on renvoie le bon code
Vérifier que si la communication avec pointsetmanager à échoué on renvoie bien le code

##Test de performance :
*Le but est de tester la capacité du code a ne pas ramer sous un gros stress*

Vérifier si l’appli ne ralenti pas si il y a 100 points ou plus
Vérifier si l’appli charge les triangles rapidements

##Test de qualité fait avec ruff : 
Vérifier que les commentaires sont bien présents
Vérifier qu’il n’y a pas de variables inutilisées
Vérifier la robustesse des input
Vérifier qu’il n’y a pas de condition inutile 
Vérifier qu’il n’y a pas de bibliothèques importé inutilisées
