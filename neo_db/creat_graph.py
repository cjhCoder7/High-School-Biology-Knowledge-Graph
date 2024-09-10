from config import graph

graph.delete_all()  # 删除已有的所有内容
with open("./raw_data/relation.txt") as f:
    for line in f.readlines():
        rela_array = line.strip("\n").split(",")
        print(rela_array)
        graph.run("MERGE(p: Person{Name: '%s'})" % (rela_array[0]))
        graph.run("MERGE(p: Person{Name: '%s'})" % (rela_array[2]))
        graph.run(
            "MATCH(e: Person), (cc: Person) \
            WHERE e.Name='%s' AND cc.Name='%s'\
            CREATE(e)-[r:%s{relation: '%s'}]->(cc)\
            RETURN r"
            % (rela_array[0], rela_array[2], rela_array[1], rela_array[1])
        )
