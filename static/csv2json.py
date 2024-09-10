import json

# 定义文件路径
relation_file_path = "relation.txt"
output_file_path = "data.json"

# 读取 relation.txt 文件
with open(relation_file_path, "r", encoding="GBK") as file:
    lines = file.readlines()

# 构建 JSON 对象
data = []
links = []
name_to_index = {}

for line in lines:
    parts = line.strip().split(",")
    if len(parts) == 3:
        source, relationship, target = parts

        if source not in name_to_index:
            name_to_index[source] = len(data)
            data.append({"name": source})

        if target not in name_to_index:
            name_to_index[target] = len(data)
            data.append({"name": target})

        links.append(
            {
                "source": name_to_index[source],
                "target": name_to_index[target],
                "value": relationship,
            }
        )

result = {"data": data, "links": links}

# 将结果保存为 JSON 文件
with open(output_file_path, "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)

print(f"转换完成，JSON文件已保存到: {output_file_path}")
