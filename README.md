# API avce Mongo et Neo4J
Le but de ce projet était d'appréhender les bases de données MongoDB et Neo4J avec python pour effectuer une API. Pour ce projet, nous avons utilisé les échantillons de données proposées par les deux bases de données : movies dans sample_mflix pour mongo et movies avec plus de 28000 noeuds sur neo4j.

## Installation

Pour lancer l'application, il vous faudra d'abord installer toutes les librairies associées.
```bash
$ pip install -r requirements.txt
```

Dans le fichier connection.py, définissez les variables suivantes pour vous connecter à vos bases de données neo4j et mongo (pour la base de données Mongo, une instance est déjà défini et **normalement** fonctionne) :  

```python
client = MongoClient("mongodb+srv://user:password@adresseDuCluster/") #URI de connexion à une instance MongoDB
db = client.dataBase #Définissez le nom de la dataBase (fixé à sample_mflix de base)
collection = db.collection #Définissez le nom de la collection (fixé à movies de base) 


driver = GraphDatabase.driver(
  "bolt://addresse:port", #URI à une DB neo4J
  auth=basic_auth("neo4j", "password")) #Définir le mot de passe
```

Assurez vous au préalable que ces bases de données contiennent bien les Databases movies sur Mongo et neo4j.

## Lancer l'API flask
```bash
$ flask --app main.py run --port 8000
```

Ou par cette commande
```bash
$ python main.py
```

## Routes et fonctionnalités associés
- **/** : Lister tous les films d'une base de données
- **/getMoviesByTitleOrCast/<name>** : Lister un film - le nom du film ou le nom d'un acteur du film est donnée en paramètre
- **/getApproximatelyMovies/<movies_name>** : Lister un film - le nom du film ou le nom d'un acteur du film est donnée en paramètre. Ces noms peuvent être mis de toutes les manières (majuscules, début du nom du film seulement...)
- **/getReviewersByMovie/<movies_name>** : Lister les utilisateurs qui ont émis une critique d'un film - le nom du film est donné en paramètre
- **/getMoviesReviewed/<person>>** : Lister les utilisateurs avec leur nombre de films qu'ils ont critiqués accompagnés de les noms des films - le nom de l'utilisateur est donné en paramètre
- **/similarity** : retourne le nombre de films commun entre les bases de données mongoDB et neo4j
- **/update/<title>** : Mettre à jour les informations par rapport à un film - le nom du film devant être changé est donné en paramètre. Les informations modifiées doivent être données sous format json. (Les informations données doivent être les suivantes : le nom des acteurs, les genres du film, le nom du film, l'année du film)

## Lancer et tester les routes avec Postamn
  
  Pour tester l'API, je vous invite à utiliser Postman et à importer cette collection via l'API de Postman : https://api.postman.com/collections/27816364-2675e944-4734-40c2-bcf0-d9b7ea5e3ef8?access_key=PMAT-01H2G3KJ6VPN8SY5TN22A50Y7D.
  
  Vous pouvez importer la collection directement sur postman et indiquer l'API dans le champ dédié comme ci-dessous.
  
  <img width="482" alt="image" src="https://github.com/Ant01ne2/Movies/assets/96232442/1c9a7051-15dc-4c11-b191-9e193a5ee55a">
  
Cette collection contient différents dossiers qui correspondent à toutes les routes citées précédemment, chacun de ces dossiers comporte :
  - Une requête pré-définie dont vous pouvez modifier le paramètre à mettre en entrée ;
  - Une requête avec un paramètre déjà défini servant d'exemple.
