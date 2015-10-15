from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.types import *


conf = SparkConf().setAppName("SODA").setMaster("local")
sc = SparkContext(conf=conf)

sqlContext = SQLContext(sc)


taxi_a2_1 = sc.textFile("/project/nlp/soda/taxdata/part-00008",use_unicode=False).map(lambda col: col.split(",")).map(lambda
line:(line[0], line[2], line[7], float(line[8]), float(line[9])))

fieldName = ['ID', 'empty', 'send', 'longitude', 'lattitude']

field = [StructField("ID", StringType(), False),StructField('empty', StringType(), False),
         StructField('send', StringType(), False),StructField('longitude', DoubleType(), False),
         StructField('lattitude', DoubleType(), False)]

schema = StructType(field)


taxi_a2_2 = sqlContext.createDataFrame(taxi_a2_1, schema)

taxi_a2_2.show(1)
taxi_a2_2.take(1)


taxi_a2_3 = taxi_a2_2.filter( taxi_a2_2.longitude>121.460845)
#taxi_a2_4 = taxi_a2_3.filter( taxi_a2_3.longitude<121.470845)
#taxi_a2_5 = taxi_a2_4.filter( taxi_a2_4.lattitude>31.205884)
#taxi_a2_6 = taxi_a2_5.filter( taxi_a2_5.lattitude<31.215884)

taxi_a2_3.show(10)

taxi_a2_3.count()
##661127
#taxi_a2_3.map(lambda line: (line.ID, line.empty, line.send, line.longitude, line.lattitude)).coalesce(1,True).saveAsTextFile("/user/nli26/taxia2")

