import csv,json


with open('srms.csv',encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)

with open("data.json","w",encoding="utf-8") as f:
    json.dump(data,f, indent=2)
    
