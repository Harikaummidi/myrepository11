from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

data = sc.textFile("/FileStore/tables/wordcount.txt")

lines = data.flatMap(lambda line: line.split(" "))

words = lines.map(lambda word: (word, 1))
wordCounts = words.reduceByKey(lambda a,b:a+b)
print(wordCounts.collect())







