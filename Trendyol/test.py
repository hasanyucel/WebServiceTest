import json
import collections
import sqlite3

conn = sqlite3.connect('etipaen.db')
cursor = conn.cursor()
cursor.execute("SELECT barcode,listPrice,salePrice FROM buybox2")
rows = cursor.fetchall()
print(rows)
objects_dict = {}
objects_dict["items"] = []
for row in rows:
    d = collections.OrderedDict()
    d["barcode"] = row[0]
    d["listPrice"] = row[1]
    d["salePrice"] = row[2]
    objects_dict["items"].append(d)

j = json.dumps(objects_dict,indent=4)
with open("products.json", "w") as f:
    f.write(j)
conn.close()