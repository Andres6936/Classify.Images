import logging
import sqlite3

from sqlite3 import Cursor
from typing import AnyStr

from Source.Classifier.LoaderFiles import GetListFilesRecursivelyAt
from Source.Classifier.Model import Classifier


def ImageAlreadyClassified(imagePath: AnyStr, cursor: Cursor):
    """
    Returns:
        Return True if the image already classified, False otherwise.

    Note:
        it is assumed that any image name already in the database
        has been classified.
    """
    response = cursor.execute(f"SELECT COUNT(1) FROM Images WHERE Name = '{imagePath}'")
    count = response.fetchone()[0]
    return True if count > 0 else False


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s][%(levelname)s][%(threadName)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    connection = sqlite3.connect("Images.sqlite")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Images(Name TEXT PRIMARY KEY, Label TEXT, Probability REAL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Errors(Name TEXT PRINARY KEY, Cause TEXT)")
    images: list[AnyStr] = GetListFilesRecursivelyAt("Pre-Trainer/**/*.webp")
    classifier = Classifier()

    for imageClassify in images:
        logging.info(f"Start classify of image: {imageClassify}")
        if ImageAlreadyClassified(imageClassify, cursor):
            logging.info(f"Image already classified, skipping image")
            continue

        try:
            prediction = classifier.ClassifyImage(imageClassify)
            cursor.execute(
                "INSERT INTO Images VALUES (?, ?, ?)",
                (imageClassify, prediction['Label'], prediction['Probability'].item()))
            logging.info(
                f"Inserted register in database with values ({prediction['Label']}, {prediction['Probability'].item()})")
        except Exception as e:
            logging.warning(f"Error classifying image: {imageClassify}, saving information of error")
            cursor.execute("INSERT INTO Errors VALUES (?, ?)", (imageClassify, str(e)))
        finally:
            connection.commit()
