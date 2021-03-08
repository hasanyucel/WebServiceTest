import requests
import json
from base64 import b64encode

end_point_ = "https://stageapi.trendyol.com/stagesapigw/" # Test: https://stageapi.trendyol.com/stagesapigw/ - Prod: https://api.trendyol.com/sapigw/

seller_id_ = "2738"
user_ = "LPQcjOdyyg5531DAj8J8"
password_ = "H6VTAMwr2kAAIeRMfpRG"
jsonfile_ = "stok_guncelle.json"

#OOP'ye göre düzenleme yapılacak.
#Create json file methodu yazılacak.

def update_stock_and_price(end_point,seller_id,user,password,jsonfile):
    price_update_url = f"{end_point}suppliers/{seller_id}/products/price-and-inventory"
    with open(jsonfile) as update_file:
        json_data = json.load(update_file)
    print(json.dumps(json_data, indent=4))

    headers = {
        "Authorization": "Basic {}".format(
            b64encode(bytes(f"{user}:{password}", "utf-8")).decode("ascii")),
        "Content-Type": "application/json",
        "user-agent":f"{seller_id} - SelfIntegration"
    }
    response = requests.request("POST", price_update_url, headers=headers, data=json.dumps(json_data))
    print(response.text)

update_stock_and_price(end_point_,seller_id_,user_,password_,jsonfile_)