from py2neo import Graph

graph = Graph("bolt://localhost:7687", auth=("neo4j", "123456789"))
