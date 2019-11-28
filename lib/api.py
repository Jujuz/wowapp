import urllib3
import requests
import json
import sys


"""
- Import the class with from lib.api import api
- Instanciate the class with x = api()
- Call the class with x.get_date(2112)

"""


class api():


    def get_token(self):

        url = "au.api.blizzard.com"
        headers = {
            'Host': "au.api.blizzard.com",
            'grant_type': "authorization_token",
            'client_id': "db1633a0b8cf4f50af81e8aad85de1a9",
            'client_secret': "MDPYUuGm46A09oC426vsBDWV0Wq8loo7"
        }


        response = requests.request("POST", url, headers=headers)
        print(response)


    def get_data(self, i):
        # Target url for required API GET request
        # self.i = 2144
        url = f"https://us.api.blizzard.com/wow/achievement/{i}"
        # url = "https://us.api.blizzard.com/wow/guild/Barthilas/Vertigo"
        token = "UScE2zyIRwh7K1EDUSdThXMObAQmulWt63"

        # Auth headers
        headers = {
            'Authorization': f"Bearer {token}",
            'User-Agent': "PostmanRuntime/7.13.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "6b6fa52e-f233-4213-afc7-b84d3d79bcaf,9a7317ac-8127-4dc9-b4b5-91039fcf1975",
            'Host': "au.api.blizzard.com",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        # # Sends request
        response = requests.request("GET", url, headers=headers)
        # raw = response.text
        parsed = json.loads(response.text)
        pretty_dat = (json.dumps(parsed, indent=4, sort_keys=True))

        # print(pretty_dat)
        with open('data.txt', 'a+') as outfile:
            outfile.write(pretty_dat)
            outfile.write("\n")
            outfile.close()

    def harvest(self):
        data = json.load

        for i in range(99):
            print(i)
            self.get_data(i)
