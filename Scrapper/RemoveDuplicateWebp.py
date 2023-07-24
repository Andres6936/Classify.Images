import glob
import hashlib
import logging
import os
from pathlib import Path
from typing import List, AnyStr

BLOCK_SIZE = 65536
GLOB_CRITERIA = "../12M_12_025_100"


def CalculateHash(filepath: Path) -> str:
    filehash = hashlib.sha256()
    with open(filepath, 'rb') as file:
        binaryBlock: AnyStr = file.read(BLOCK_SIZE)
        while len(binaryBlock) > 0:
            filehash.update(binaryBlock)
            binaryBlock: AnyStr = file.read(BLOCK_SIZE)
    return filehash.hexdigest()


def RemoveRepeatFiles(directory: str, repeatable: dict[str, str]):
    logging.info("Removing repeat files in directory: " + directory)
    for hashfile in repeatable:
        filenames = repeatable[hashfile].rstrip(',').split(',')
        for file in filenames:
            logging.info("Removing file: " + file)
            os.remove(Path(directory, file))


def RunRemoveDuplicateWebp():
    logging.info("Start remove duplicate webp")
    directories: List[AnyStr] = glob.glob(GLOB_CRITERIA)
    for directory in directories:
        hashtable: dict[str, int] = {}
        repeatable: dict[str, str] = {}
        logging.info(f"Start calculate hash for directory: {directory}")
        for file in Path(directory).glob("*.webp"):
            logging.info(f"Calculate hash for file: {file.name}")
            hashfile: str = CalculateHash(file)
            if hashfile in hashtable:
                logging.info(f"Found repeat hash by file: {file.name}")
                repeatFiles: str = repeatable.get(hashfile, '')
                repeatFiles: str = ','.join([file.name, repeatFiles])
                repeatable[hashfile] = repeatFiles

                repeatCount: int = hashtable[hashfile]
                repeatCount: int = repeatCount + 1
                hashtable[hashfile] = repeatCount
            else:
                hashtable[hashfile] = 1
        logging.info("Removing all repeat files for directory: " + directory)
        RemoveRepeatFiles(directory, repeatable)
        logging.info("Finish calculate hash and remove duplicate files in directory: " + directory)
