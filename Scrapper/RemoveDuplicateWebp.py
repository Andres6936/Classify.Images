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
    repeatable = {}
    directories: List[AnyStr] = glob.glob(GLOB_CRITERIA)
    for directory in directories:
        for file in Path(directory).glob("*.webp"):
            hashfile: str = CalculateHash(file)
            if hashfile in hashtable:
                repeatFiles = repeatable.get(hashfile, '')
                repeatFiles = ','.join([file.name, repeatFiles])
                repeatable[hashfile] = repeatFiles

                repeatCount = hashtable[hashfile]
                repeatCount = repeatCount + 1
                hashtable[hashfile] = repeatCount
            else:
                hashtable[hashfile] = 1
