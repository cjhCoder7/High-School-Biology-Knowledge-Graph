from neo_db.config import graph
import codecs
import os
import json
import base64


def query(name):
    data = graph.run(
        "match(p )-[r]->(n:Person{Name:'%s'}) return  p.Name,r.relation,n.Name\
        Union all\
    match(p:Person {Name:'%s'}) -[r]->(n) return p.Name, r.relation, n.Name"
        % (name, name)
    )
    data = list(data)
    return get_json_data(data)


def get_json_data(data):
    json_data = {"data": [], "links": []}
    d = []

    for i in data:
        # print(i["p.Name"], i["r.relation"], i["n.Name"], i["p.cate"], i["n.cate"])
        d.append(i["p.Name"])
        d.append(i["n.Name"])
        d = list(set(d))
    name_dict = {}
    count = 0
    for j in d:
        j_array = j.split("_")

        data_item = {}
        name_dict[j_array[0]] = count
        count += 1
        data_item["name"] = j_array[0]
        json_data["data"].append(data_item)
    for i in data:

        link_item = {}

        link_item["source"] = name_dict[i["p.Name"]]

        link_item["target"] = name_dict[i["n.Name"]]
        link_item["value"] = i["r.relation"]
        json_data["links"].append(link_item)

    return json_data
