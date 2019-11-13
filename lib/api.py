import urllib3
import requests
import json


class api():


    def get_data(self, url):
        # Target url for required API GET request
        self.url = "https://us.api.blizzard.com/wow/achievement/2144"

        # url = "https://us.api.blizzard.com/wow/guild/Barthilas/Vertigo"

        token = "US22faCBq46fY7Dt2L1NsNPlqabrSNyup7"

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
        print(pretty_dat)

