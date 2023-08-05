import sqlite3

from Source.Classifier.LoaderFiles import GetListFilesRecursivelyAt
from Source.Classifier.Model import Classifier

connection = sqlite3.connect("Images.sqlite")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Images(Name TEXT PRIMARY KEY, Label TEXT)")
#imagesToClassify = GetListFilesRecursivelyAt("Pre-Trainer/**/*.webp")
classifier = Classifier()
classifier.ClassifyImage()

#for imageClassify in imagesToClassify:
#    label = classifier.ClassifyImage()
