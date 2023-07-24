import glob
import hashlib
import logging
from pathlib import Path
from typing import List, AnyStr

BLOCK_SIZE = 65536
GLOB_CRITERIA = "../12M_12_025_100"


def CalculateHash(filepath: Path) -> str:
    filehash = hashlib.sha256()
    with open(filepath, 'rb') as file:
        binaryBlock = file.read(BLOCK_SIZE)
        while len(binaryBlock) > 0:
            filehash.update(binaryBlock)
            binaryBlock = file.read(BLOCK_SIZE)
    return filehash.hexdigest()


def RunRemoveDuplicateWebp():
    logging.info("Start remove duplicate webp")
    hashtable = {}
    directories: List[AnyStr] = glob.glob(GLOB_CRITERIA)
    for directory in directories:
        for file in Path(directory).glob("*.webp"):
            hashfile: str = CalculateHash(file)
            if hashfile in hashtable:
                repeatFiles = hashtable[hashfile]
                repeatFiles = repeatFiles + ',' + file.name
                hashtable[hashfile] = repeatFiles
            else:
                hashtable[hashfile] = file.name
