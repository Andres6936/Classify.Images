import logging
import argparse

from Scrapper.Actions import Actions
from Scrapper.RemoveDuplicateWebp import RunRemoveDuplicateWebp
from Scrapper.ScrapperWebp import RunScrapperWebp

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s][%(levelname)s][%(threadName)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", help=f"Choice between this actions: {list(Actions)}", type=str)
    args = parser.parse_args()
    if args.action == Actions.SCRAPPER_WEBP.name:
        RunScrapperWebp()
    elif args.action == Actions.REMOVE_DUPLICATE_WEBP.name:
        RunRemoveDuplicateWebp()
