import json

buyboxProducts = {
  "items": [
    {"barcode": "1952084972279", "salePrice": 27.5, "listPrice": 27.5},
    {"barcode": "1952084972280", "salePrice": 270.5, "listPrice": 270.5},
    {"barcode": "1952084972281", "salePrice": 270.5, "listPrice": 270.5}
  ]
}

y = json.dumps(buyboxProducts, indent=4)


print(y)
