import logging
import sqlite3

from Source.Classifier.LoaderFiles import GetListFilesRecursivelyAt
from Source.Classifier.Model import Classifier


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s][%(levelname)s][%(threadName)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    connection = sqlite3.connect("Images.sqlite")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Images(Name TEXT PRIMARY KEY, Label TEXT, Probability REAL)")
    images = GetListFilesRecursivelyAt("Pre-Trainer/**/*.webp")
    classifier = Classifier()

    for imageClassify in images:
        logging.info(f"Start classify of image: {imageClassify}")
        prediction = classifier.ClassifyImage(imageClassify)
        cursor.execute(
            "INSERT INTO Images VALUES (?, ?, ?)",
            (imageClassify, prediction['Label'], prediction['Probability'].item()))
        connection.commit()
        logging.info(f"Inserted register in database with values ({prediction['Label']}, {prediction['Probability'].item()})")
