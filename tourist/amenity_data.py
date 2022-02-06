import overpy
import pandas as pd

def query_generator(param):
    prefix = "[out:json][timeout:25];area(3604583125)->.searchArea;("
    node = "node['amenity'={0}](area.searchArea);".format(param)
    way = "way['amenity'={0}](area.searchArea);".format(param)
    relation = "relation['amenity'={0}](area.searchArea);".format(param)
    suffix = ");out body;>;out skel qt;"
    query = prefix + node + way + relation + suffix
    api = overpy.Overpass()
    result = api.query(query)

    list_of_node_tags = []  # initializing empty list , we'll use it to form a dataframe .
    for node in result.nodes:  # from each node , get the all tags information
        node.tags['latitude'] = node.lat
        node.tags['longitude'] = node.lon
        node.tags['id'] = node.id
        list_of_node_tags.append(node.tags)
    print(list_of_node_tags)
    data_frame = pd.DataFrame(list_of_node_tags)  # forming a pandas dataframe using list of dictionaries
    data_frame.to_csv('output_data.csv')

query_generator("'bar'")
