import glob

from typing import AnyStr


def GetListFilesRecursivelyAt(path: str) -> list[AnyStr]:
    return glob.glob(path, recursive=True)
