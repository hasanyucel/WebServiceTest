from Trendyol.guncelle import Trendyol as ty 
import timeit
import json

seller_id = "2738"
user = "LPQcjOdyyg5531DAj8J8"
password = "H6VTAMwr2kAAIeRMfpRG"
test = "https://stageapi.trendyol.com/stagesapigw/"
prod = "https://api.trendyol.com/sapigw/"
db = "etipaen.db"
updateJson = "productUpdate.json"

user1 = ty(test,seller_id,user,password) #Nesne
#products = user1.updatePriceAndInventory(jsonfile)
#print(products)
#user1.getProductListPrice("1952084972279")
#productList = [('1952084972279', 100.5, 99), ('1952084972280', 115.3, 100)]
#user1.createUpdateJsonFileFromList(productList)
#user1.createUpdateJsonFileFromSqlite(db)
start = timeit.timeit()
lst = user1.getBuyboxListFromPostgre()
print(lst)
user1.createUpdateJsonFileFromList(lst)
result = user1.updatePriceAndInventory(updateJson)
y = json.loads(result)
print(y["batchRequestId"])
batchRes = user1.checkBatchRequestResult(y["batchRequestId"])
z = json.loads(batchRes)
json_formatted_str = json.dumps(z, indent=2)
print(json_formatted_str)
end = timeit.timeit()
print(start - end)


