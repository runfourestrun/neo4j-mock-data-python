from neo4jclient import Neo4jClient,Model
from neo4jclient.TransactionFunctions import write_Schedule
import os
from random import choices

from graphdatascience import GraphDataScience



def buildCapacityModel(id,technician):
    return Model.Capacity(id,technician)


def buildSchedules(id,technician):
    return Model.Schedule(id,technician)


if __name__ == '__main__':
    #Create neo4j client
    url = os.environ.get('NEO4J_CENTRAL_URI')
    username = os.environ.get('NEO4J_CENTRAL_USER')
    password = os.environ.get('NEO4J_CENTRAL_PASSWORD')
    database = 'neo4j'
    neo4j = Neo4jClient(url=url, username=username, password=password,database=database)


    #Read Neo4j to get existing Nodes as Python Neo4j Records
    plant_location_records = neo4j.read("MATCH (pl:PlantLocation) RETURN pl.id")
    technician_records = neo4j.read("MATCH (t:Technician) RETURN t.id")
    technician_ids = [record['t.id'] for record in technician_records]
    plant_location_ids = [record['pl.id'] for record in plant_location_records]

    #Get length of records
    technician_len = len(technician_ids)
    plant_location_len = len(plant_location_ids)

    #Id field to be used in Model.Schedule & Model.Capacity
    ids = range(0,technician_len)

    # zipping iterables ids & technician ids
    inputs = zip(ids,technician_ids)

    scheduleObjects = [vars(buildSchedules(id,technician)) for id,technician in inputs]
    params = {'params':scheduleObjects}


    neo4j.write(tx_func=write_Schedule,parameters=params)

    gds = GraphDataScience()
    g, _ = gds.graph.project.cypher()
    test = gds.nodeSimilarity.write













