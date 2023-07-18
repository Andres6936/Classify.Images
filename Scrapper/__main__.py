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
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s][%(levelname)s][%(threadName)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    with Pool(processes=MAXIMUM_THREADS_SPAWN) as pool:
        for index in range(START, END, STEP):
            pool.starmap_async(ScrapperImage, [(index if index == START else index + 1, index + STEP)])
        pool.close()
        pool.join()
