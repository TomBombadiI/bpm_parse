import json, csv

js = open('res.json', encoding='utf8').read()

res = json.loads(js)

with open('res.csv', 'w', encoding='utf8', newline="") as csv_file:
    writer = csv.writer(csv_file)
    for row in res:
        writer.writerow(row)