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
#Request Resultlarını inceleyip problemli olanları döndüren bir fonksiyon yaz.

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

def checkBatchRequestResult(end_point,seller_id,user,password,batchRequestId):
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

def getApprovedProducts(end_point,seller_id,user,password):

    url = f"{end_point}suppliers/{seller_id}/products?page=1&size=2&approved=true"

    payload={}
    headers = {
        "Authorization": "Basic {}".format(
            b64encode(bytes(f"{user}:{password}", "utf-8")).decode("ascii")),
        "Content-Type": "application/json",
        "user-agent":f"{seller_id} - SelfIntegration"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return(response.text)

def getProductListPrice(end_point,seller_id,user,password,barcode):

    url = f"{end_point}suppliers/{seller_id}/products?approved=true&barcode={barcode}"
    payload={}
    headers = {
        "Authorization": "Basic {}".format(
            b64encode(bytes(f"{user}:{password}", "utf-8")).decode("ascii")),
        "Content-Type": "application/json",
        "user-agent":f"{seller_id} - SelfIntegration"
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    employee_dict = json.loads(response.text) 
    print("List Price: ",employee_dict["content"][0]["listPrice"])
    print("Sale Price: ",employee_dict["content"][0]["salePrice"])

getProductListPrice(end_point_,seller_id_,user_,password_,"2100000078727")
#products = getApprovedProducts(end_point_,seller_id_,user_,password_)
#print(json.dumps(json.loads(products), sort_keys=True, indent=4, separators=(",", ": ")))

#result = updatePriceAndInventory(end_point_,seller_id_,user_,password_,jsonfile_)
#result = json.loads(result)

#print(checkBatchRequestResult(end_point_,seller_id_,user_,password_,result['batchRequestId']))