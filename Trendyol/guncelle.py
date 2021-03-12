import requests
import json
import collections
from base64 import b64encode
import sqlite3 #Test
import timeit

# Test: https://stageapi.trendyol.com/stagesapigw/ - Prod: https://api.trendyol.com/sapigw/
test = "https://stageapi.trendyol.com/stagesapigw/"
prod = "https://api.trendyol.com/sapigw/"
db = "etipaen.db"
class Trendyol:
    def __init__(self,end_point,seller_id,user,password):
        self.end_point = end_point
        self.seller_id = seller_id
        self.user = user
        self.password = password

    def updatePriceAndInventory(self,jsonfile):
        url = f"{self.end_point}suppliers/{self.seller_id}/products/price-and-inventory"
        with open(jsonfile) as update_file:
            json_data = json.load(update_file)
        print(json.dumps(json_data, indent=4))
        headers = {
            "Authorization": "Basic {}".format(
                b64encode(bytes(f"{self.user}:{self.password}", "utf-8")).decode("ascii")),
            "Content-Type": "application/json",
            "user-agent":f"{self.seller_id} - SelfIntegration"
        }
        response = requests.request("POST", url, headers=headers, data=json.dumps(json_data))
        return(response.text)

    def checkBatchRequestResult(self,batchRequestId):
        url = f"{self.end_point}suppliers/{self.seller_id}/products/batch-requests/{batchRequestId}"
        payload={}
        headers = {
            "Authorization": "Basic {}".format(
                b64encode(bytes(f"{self.user}:{self.password}", "utf-8")).decode("ascii")),
            "Content-Type": "application/json",
            "user-agent":f"{self.seller_id} - SelfIntegration"
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return(response.text)

    def getApprovedProducts(self):
        url = f"{self.end_point}suppliers/{self.seller_id}/products?page=1&size=2&approved=true"
        payload={}
        headers = {
            "Authorization": "Basic {}".format(
                b64encode(bytes(f"{self.user}:{self.password}", "utf-8")).decode("ascii")),
            "Content-Type": "application/json",
            "user-agent":f"{self.seller_id} - SelfIntegration"
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return(response.text)

    def getProductListPrice(self,barcode):
        url = f"{self.end_point}suppliers/{self.seller_id}/products?approved=true&barcode={barcode}"
        payload={}
        headers = {
            "Authorization": "Basic {}".format(
                b64encode(bytes(f"{self.user}:{self.password}", "utf-8")).decode("ascii")),
            "Content-Type": "application/json",
            "user-agent":f"{self.seller_id} - SelfIntegration"
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        employee_dict = json.loads(response.text) 
        print("List Price: ",employee_dict["content"][0]["listPrice"])
        print("Sale Price: ",employee_dict["content"][0]["salePrice"])

    def createUpdateJsonFileFromList(self,lst):
        objects_dict = {}
        objects_dict["items"] = []
        for row in lst:
            d = collections.OrderedDict()
            d["barcode"] = row[0]
            d["listPrice"] = row[1]
            d["salePrice"] = row[2]
            objects_dict["items"].append(d)

        j = json.dumps(objects_dict,indent=4)
        with open("productUpdate.json", "w") as f:
            f.write(j)


    #Request Resultlarını inceleyip problemli olanları döndüren bir fonksiyon yaz.

#seller_id = "2738"
#user = "LPQcjOdyyg5531DAj8J8"
#password = "H6VTAMwr2kAAIeRMfpRG"
user1 = Trendyol(test,'2738','LPQcjOdyyg5531DAj8J8','H6VTAMwr2kAAIeRMfpRG')
#products = user1.updatePriceAndInventory(jsonfile)
#print(products)
#user1.getProductListPrice("1952084972279")

start = timeit.timeit()
productList = [('1952084972279', 100.5, 99), ('1952084972280', 115.3, 100)]
user1.createUpdateJsonFileFromList(productList)
end = timeit.timeit()
print(start - end)