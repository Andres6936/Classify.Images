import time
import requests

from requests.exceptions import JSONDecodeError

# Range calculated from 12_000_000 to 12_025_100
# Range calculated from 12_025_100 to 12_051_821
# Range calculated from 12_051_821 to 12_102_326
START = 12_102_326
END = 19_999_999

# Used for determine the time of wait between request
STEP = 5_000
URL = 'https://carulla.vtexassets.com/arquivos/ids/'


def ScrapperImage(start: int, end: int) -> None:
    print(f"Start request {start} to {end}")
    for i in range(start, end):
        stream = requests.get(URL + str(i))
        print(f"Request: {i}")
        # Verify if the URL is empty response
        try:
            response = stream.json()
            if response['statusCode'] == 404:
                continue
        except JSONDecodeError as ignored:
            pass
        # The response is a valid image, parse and save
        with open('../Data/' + str(i) + '.webp', 'wb') as file:
            print(f"Writing file: {i}.webp")
            file.write(stream.content)


if __name__ == '__main__':
    for index in range(START, END, STEP):
        ScrapperImage(index, index + STEP)
        time.sleep(10)
