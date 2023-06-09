from pymongo import MongoClient
from neo4j import GraphDatabase, basic_auth


client = MongoClient("mongodb+srv://username:password@cluster0.uqk1rfv.mongodb.net/")
db = client.sample_mflix
collection = db.movies


driver = GraphDatabase.driver(
  "bolt://3.216.132.126:7687",
  auth=basic_auth("neo4j", "accruals-attraction-furs"))

