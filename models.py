from connection import collection
import re

def get_artist():
    rec = collection.find()
    return {'movies': [movies['title'] for movies in rec]}

def get_bymovies(name):
    title = collection.find({'title': name})
    cast = collection.find({'cast': name})

    if ([movies['title'] for movies in title]!=[]):
        rec = collection.find({'title': name})
        return {'resultat': [{'title': movies['title'],
                              'year': movies['year'],
                              'genres': movies['genres'],
                              'cast': movies['cast']} for movies in rec] }
    
    elif ([movies['cast'] for movies in cast]!=[]):
        rec = collection.find({'cast': name})
        return {'resultat': [{'title': movies['title'],
                              'year': movies['year'],
                              'genres': movies['genres'],
                              'cast': movies['cast']} for movies in rec]}
    
    else:
        return ('No Data')


def get_byApproResearch(name):
    regex = re.compile('.*' + re.escape(name) + '.*', re.IGNORECASE)
    title = collection.find({'title': {'$regex': regex}})
    cast = collection.find({'cast': {'$regex': regex}})
    
    if ([movies['title'] for movies in title]!=[]):
        rec = collection.find({'title': {'$regex': regex}})
        return {'movies': [movies['title'] for movies in rec]}
    
    elif ([movies['cast'] for movies in cast]!=[]):
        rec = collection.find({'cast': {'$regex': regex}})
        return {'movies': [movies['title'] for movies in rec]}
    
    else:
        return ('No Data')


def get_bycast(name):
    rec = collection.find({'cast': name})
    return {'movies': [movies['title'] for movies in rec]}
