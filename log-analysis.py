#---- SPARK ----
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, size

appName = "Microservices Logs Analyzer"
master = "local"

# Create Spark session
spark = SparkSession.builder \
    .appName(appName) \
    .master(master) \
    .getOrCreate()

spark.sparkContext.setLogLevel("DEBUG")

# Create DF by reading from log files
df = spark.read.text('app.log')
df.show()

# Filtering NOT_FOUND
df.filter(col('value').contains('404 NOT_FOUND')).head(5)

#Filtering Host
df.filter(col('value').like('%Host:%')).show(5)

#Further Filtering Host other than Localhost
df.filter(col('value').like('%Host:%')).filter(~col('value').like('%localhost%')).show()