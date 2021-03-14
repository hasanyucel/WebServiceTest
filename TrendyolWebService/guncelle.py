import requests
import json
import collections
from base64 import b64encode
import sqlite3 #Test
import psycopg2 #Postgre

class Trendyol_API:
    def __init__(self,end_point,seller_id,user,password):
        self.end_point = end_point
        self.seller_id = seller_id
        self.user = user
        self.password = password

    def updatePriceAndInventory(self,jsonfile):
        url = f"{self.end_point}suppliers/{self.seller_id}/products/price-and-inventory"
        with open(jsonfile) as update_file:
            json_data = json.load(update_file)
        #print(json.dumps(json_data, indent=4))
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
        url = f"{self.end_point}suppliers/{self.seller_id}/products?approved=true"
        payload={}
        headers = {
            "Authorization": "Basic {}".format(
                b64encode(bytes(f"{self.user}:{self.password}", "utf-8")).decode("ascii")),
            "Content-Type": "application/json",
            "user-agent":f"{self.seller_id} - SelfIntegration"
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        result = json.loads((response.text))
        return result["batchRequestId"]

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

    def createUpdateJsonFileFromSqlite(self,db):

        conn = sqlite3.connect(db)
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
        with open("productUpdate.json", "w") as f:
            f.write(j)
        conn.close()

    def getBuyboxListFromPostgre(self):
        db = psycopg2.connect(user = "postgres",
                      password = "postgres",
                      host = "localhost",
                      port = "5432",
                      database = "etipaen")
        imlec = db.cursor()
        imlec.execute("""Select * from buybox""")
        rows = imlec.fetchall()
        return(rows)

        
    #Request Resultlarını inceleyip problemli olanları döndüren bir fonksiyon yaz.
    #Kullanıcının Tüm satışa açık ürünlerini listeye alan fonksiyon ve postgresql tablosuna insert eden fonksiyon
    #listPrice salePrice'dan küçük olamaz. Kontrol et.



