import sqlite3

from Source.Classifier.LoaderFiles import GetListFilesRecursivelyAt
from Source.Classifier.Model import ClassifyImage

connection = sqlite3.connect("Images.sqlite")
cursor = connection.cursor()
cursor.execute("CREATE TABLE Images(Name TEXT PRIMARY KEY, Label TEXT)")
imagesToClassify = GetListFilesRecursivelyAt("Pre-Trainer/**/*.webp")

for imageClassify in imagesToClassify:
    label = ClassifyImage()
