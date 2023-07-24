import requests
import logging

from multiprocessing.pool import Pool
from requests.exceptions import JSONDecodeError

START = 12_750_000
END = 12_999_999

MAXIMUM_THREADS_SPAWN = 16
# Used for determine the time of wait between request
STEP = 1_000
URL = 'https://carulla.vtexassets.com/arquivos/ids/'


def ScrapperImage(start: int, end: int) -> None:
    logging.info(f"Start request {start} to {end}")
    for i in range(start, end):
        stream = requests.get(URL + str(i))
        logging.info(f"Request: {i}")
        # Verify if the URL is empty response
        try:
            response = stream.json()
            if response['statusCode'] == 404:
                continue
        except JSONDecodeError:
            pass
        # The response is a valid image, parse and save
        with open('../Data/' + str(i) + '.webp', 'wb') as file:
            logging.info(f"Writing file: {i}.webp")
            file.write(stream.content)


def RunScrapperWebp():
    with Pool(processes=MAXIMUM_THREADS_SPAWN) as pool:
        for index in range(START, END, STEP):
            pool.starmap_async(ScrapperImage, [(index if index == START else index + 1, index + STEP)])
        pool.close()
        pool.join()
