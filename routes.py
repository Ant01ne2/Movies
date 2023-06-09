from flask import request, Flask
from main import app
from connection import collection, driver
from models import get_artist,get_bymovies,get_byApproResearch,get_bycast



@app.route('/')
def list_arists():
    return get_artist()

@app.route('/getMoviesByTitleOrCast/<movies_name>')
def get_byname(movies_name):
    return get_bymovies(movies_name)

@app.route('/getApproximatelyMovies/<movies_name>')
def get_byAppro(movies_name):
    return get_byApproResearch(movies_name)

@app.route('/<cast>')
def get_bynameCast(cast):
    return get_bycast(cast)

@app.route('/getReviewersByMovie/<movies_name>')
def get_actors(movies_name):
    with driver.session() as session:
        actors = session.execute_read(get_actors, movies_name)

        return([record for record in actors])
        
@app.route('/getMoviesReviewed/<person>')
def get_moviesRated(person):
    with driver.session() as session:
        numMovies, ratedMovies = session.execute_read(get_moviesRated, person)
        my_dict = {
        "num": numMovies,
        "titles": ratedMovies
        }
        return(my_dict)
    
@app.route('/similarity')
def get_similarity():
    with driver.session() as session:
        counter = session.execute_read(countSimilarMovies)
        return(counter)

#dans postman, entrer dans header : content-typ  application/json
#dans body, mettre à raw et mettrez les trois arguments json
@app.route('/update/<title>', methods=['POST']) 
def update(title):

    data = request.get_json()
    collection.update_one({'title': title},{'$set': data}, upsert=False)


    return f"user : {data['year']} - {data['title']} - {data['genres']} - {data['cast']}"

def countSimilarMovies(tx):
    mongo = collection.find()
    mongo = [movies['title'] for movies in mongo]
    
    neo4j = tx.run("""
    MATCH (m:Movie) 
    RETURN m.title
    """)
    # Access the `p` value from each record
    neo4j = [ record["m.title"] for record in neo4j ]

    ensembleMongo = set(mongo)
    ensembleNeo = set(neo4j)

    elements_communs = ensembleMongo & ensembleNeo

    nombre_elements_communs = len(elements_communs)

    return "Nombre de films similaires : " + str(nombre_elements_communs)

# Unit of work
def get_actors(tx, movie): # (1)
    result = tx.run("""
    MATCH (reviewers:User)-[:RATED]->(:Movie {title: $title}) 
    RETURN reviewers.name
    """, title=movie)

    return [ record["reviewers.name"] for record in result ]

# Unit of work
def get_moviesRated(tx, person): # (1)
    result = tx.run("""
    MATCH (p:User{name: $user})-[r:RATED]->(m:Movie) 
    RETURN p.name AS userName, COUNT(m) AS numRatedMovies, COLLECT(m.title) AS ratedMovies
    """, user=person)
    
    record = result.single()
    numRatedMovies = record["numRatedMovies"]
    ratedMovies = record["ratedMovies"]
    return numRatedMovies, ratedMovies
