import sqlite3

from Source.Classifier.LoaderFiles import GetListFilesRecursivelyAt
from Source.Classifier.Model import Classifier

connection = sqlite3.connect("Images.sqlite")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Images(Name TEXT PRIMARY KEY, Label TEXT, Probability REAL)")
imagesToClassify = GetListFilesRecursivelyAt("Pre-Trainer/**/*.webp")
classifier = Classifier()

for imageClassify in imagesToClassify:
    prediction = classifier.ClassifyImage(imageClassify)
    cursor.execute(
        "INSERT INTO Images VALUES (?, ?, ?)",
        (imageClassify, prediction['Label'], prediction['Probability']))
