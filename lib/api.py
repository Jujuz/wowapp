import requests
import json

# Target url for required API GET request
url = "https://us.api.blizzard.com/wow/achievement/2144"

# url = "https://us.api.blizzard.com/wow/guild/Barthilas/Vertigo"

# Auth headers
headers = {
    'Authorization': "Bearer USI1ja1xGXzXbSmwcbjq7RoVj1xVTKtd15",
    'User-Agent': "PostmanRuntime/7.13.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "6b6fa52e-f233-4213-afc7-b84d3d79bcaf,9a7317ac-8127-4dc9-b4b5-91039fcf1975",
    'Host': "us.api.blizzard.com",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

# Sends request
response = requests.request("GET", url, headers=headers)

# Reformats output into jason and prints
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=4, sort_keys=True))
