import requests

url = "https://stageapi.trendyol.com/stagesapigw/suppliers/2738/products/batch-requests/4bcbb224-7d78-11eb-b6fc-32ab884c8ca8-1614938518"

payload={}
headers = {
  'Authorization': 'Basic TFBRY2pPZHl5ZzU1MzFEQWo4Sjg6SDZWVEFNd3Iya0FBSWVSTWZwUkc='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)