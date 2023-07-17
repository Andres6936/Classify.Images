import time
import requests
import logging

from requests.exceptions import JSONDecodeError

# Range calculated from 12_000_000 to 12_025_100
# Range calculated from 12_025_100 to 12_051_821
# Range calculated from 12_051_821 to 12_102_326
# Range calculated from 12_102_326 to 12_137_900
# Range calculated from 12_137_900 to 12_153_355
START = 12_153_355
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


def Scrapper(start: int, end: int) -> None:
    logging.info(f"Start: {start}, End: {end}")


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s][%(levelname)s][%(threadName)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    for index in range(START, END, STEP):
        # ScrapperImage(index, index + STEP)
        Scrapper(index, index + STEP)
        time.sleep(10)
