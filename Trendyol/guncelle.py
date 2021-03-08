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

def updatePriceAndInventory(end_point,seller_id,user,password,jsonfile):
    url = f"{end_point}suppliers/{seller_id}/products/price-and-inventory"
    with open(jsonfile) as update_file:
        json_data = json.load(update_file)
    print(json.dumps(json_data, indent=4))

    headers = {
        "Authorization": "Basic {}".format(
            b64encode(bytes(f"{user}:{password}", "utf-8")).decode("ascii")),
        "Content-Type": "application/json",
        "user-agent":f"{seller_id} - SelfIntegration"
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(json_data))
    return(response.text)

def getBatchRequestResult(end_point,seller_id,user,password,batchRequestId):
    url = f"{end_point}suppliers/{seller_id}/products/batch-requests/{batchRequestId}"
    payload={}
    headers = {
        "Authorization": "Basic {}".format(
            b64encode(bytes(f"{user}:{password}", "utf-8")).decode("ascii")),
        "Content-Type": "application/json",
        "user-agent":f"{seller_id} - SelfIntegration"
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return(response.text)

result = updatePriceAndInventory(end_point_,seller_id_,user_,password_,jsonfile_)
result = json.loads(result)

print(getBatchRequestResult(end_point_,seller_id_,user_,password_,result['batchRequestId']))