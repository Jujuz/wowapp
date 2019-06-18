import requests

url = "https://us.api.blizzard.com/wow/achievement/2144"

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

response = requests.request("GET", url, headers=headers)

print(response.text)

## Test Pull Request
#
#
# url = "https://us.api.blizzard.com/wow/guild/Barthilas/Vertigo"
#
# querystring = {"fields":"achievements%2Cchallenge","locale":"en_US","access_token":"US9ttrQtZUr3Dso6odnN1KuobGGTVE6kVq"}
#
# headers = {
#     'User-Agent': "PostmanRuntime/7.13.0",
#     'Accept': "*/*",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "a599c5e0-d91c-4445-a770-79588dd56d76,a12b7c76-8122-4fcd-90b8-706daa207cf3",
#     'Host': "us.api.blizzard.com",
#     'accept-encoding': "gzip, deflate",
#     'Connection': "keep-alive",
#     'cache-control': "no-cache"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response)
