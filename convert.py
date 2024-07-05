import json

# 读取输入JSON文件
with open('train_0001_of_0001.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 处理数据
processed_data = []
for item in data:
    processed_item = {
        "instruction": item["instruction"],
        "prompt": item["input"],
        "completion": item["output"],
        "history": item["history"]
    }
    processed_data.append(processed_item)

# 将处理后的数据写入输出JSON文件
with open('train.json', 'w', encoding='utf-8') as file:
    for item in processed_data:
        json.dump(item, file, ensure_ascii=False)
        file.write('\n')
