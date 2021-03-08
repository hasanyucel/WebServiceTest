import requests
import json
from base64 import b64encode

end_point = "https://stageapi.trendyol.com/stagesapigw/" # Test: https://stageapi.trendyol.com/stagesapigw/ - Prod: https://api.trendyol.com/sapigw/

seller_id = "2738"
user = "LPQcjOdyyg5531DAj8J8"
password = "H6VTAMwr2kAAIeRMfpRG"

price_update_url = f"{end_point}suppliers/{seller_id}/products/price-and-inventory"

with open('stok_guncelle.json') as json_file:
    json_data = json.load(json_file)
print(json.dumps(json_data, indent=4))

headers = {
    "Authorization": "Basic {}".format(
        b64encode(bytes(f"{user}:{password}", "utf-8")).decode("ascii")),
    "Content-Type": "application/json",
    "user-agent":f"{seller_id} - SelfIntegration"
}
response = requests.request("POST", price_update_url, headers=headers, data=json.dumps(json_data))

print(response.text)