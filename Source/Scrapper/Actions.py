from enum import Enum, unique


@unique
class Actions(Enum):
    SCRAPPER_WEBP = "SCRAPPER_WEB",
    REMOVE_DUPLICATE_WEBP = "REMOVE_DUPLICATE_WEBP"
