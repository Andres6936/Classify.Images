import sqlite3

from Source.Classifier.LoaderFiles import GetListFilesRecursivelyAt
from Source.Classifier.Model import Classifier

connection = sqlite3.connect("Images.sqlite")
cursor = connection.cursor()
cursor.execute("CREATE TABLE Images(Name TEXT PRIMARY KEY, Label TEXT)")
imagesToClassify = GetListFilesRecursivelyAt("Pre-Trainer/**/*.webp")
classifier = Classifier()

for imageClassify in imagesToClassify:
    label = classifier.ClassifyImage()
