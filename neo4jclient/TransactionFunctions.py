def exampleTxFunction(tx,params):
    '''
    Merges Material nodes to Graph
    :param tx:
    :param params:
    :return:
    '''

    tx.run(
        '''
        UNWIND $params as param
        MERGE (m:Material {id:param.MATERIAL})       
        '''
        , parameters = params
    )


def read_PlantLocation(tx):
    '''
    Reads Plant Locations
    :param tx:
    :return:
    '''

    tx.run(
    '''
    MATCH (pl:PlantLocation) RETURN pl.id
    '''
    )



def write_Schedule(tx,params):
    '''
    writes schedule
    :param tx:
    :return:
    '''

    tx.run(
    '''
    UNWIND $params as param
    MERGE (s:Schedule {id:param.id})
    ON CREATE SET 
    s.status = param.status,
    s.schedule_capacity = param.schedule_capacity,
    s.technician = param.technician
    '''
    ,parameters = params)