import time
import requests

from requests.exceptions import JSONDecodeError

URL = 'https://carulla.vtexassets.com/arquivos/ids/'

if __name__ == '__main__':
    # Range calculated from 12_000_000 to 12_025_100
    for i in range(12_025_100, 19_999_999):
        stream = requests.get(URL + str(i))
        print(f"Request: {i}")
        # Verify if the URL is empty response
        try:
            response = stream.json()
            if response['statusCode'] == 404:
                time.sleep(0.1)
                continue
        except JSONDecodeError as ignored:
            pass
        # The response is a valid image, parse and save
        with open('../Data/' + str(i) + '.webp', 'wb') as file:
            print(f"Writing file: {i}.webp")
            file.write(stream.content)
            time.sleep(0.2)
