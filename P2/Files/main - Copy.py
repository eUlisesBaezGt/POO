import json

file = open('data.json','r')
data = json.load(file)

print(data)
print(data['key1'])
print(data['key4']['key42'])