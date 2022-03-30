# Databricks notebook source
def toScala(x):
  return spark.sparkContext._jvm.scala.collection.JavaConverters.asScalaBufferConverter(x).asScala().toSeq()
def toJava(x):
  return spark.sparkContext._jvm.scala.collection.JavaConverters.seqAsJavaListConverter(x).asJava()
def toJStringArray(arr):
    jarr = sc._gateway.new_array(sc._jvm.java.lang.String, len(arr))
    for i in range(len(arr)):
        jarr[i] = arr[i]
    return jarr

# COMMAND ----------

# gateway.jvm.py4j.GatewayServer.turnLoggingOn()
sc._jvm.py4j.GatewayServer.turnLoggingOn()

# COMMAND ----------

import logging

# logger = logging.getLogger("py4j")
# logger.setLevel(logging.INFO)
# logger.addHandler(logging.StreamHandler())
logger = logging.getLogger("py4j")
logger.setLevel(logging.INFO)
logger.info("here we go")

# COMMAND ----------

log4jLogger = sc._jvm.org.apache.log4j
LOGGER = log4jLogger.LogManager.getLogger(__name__)
LOGGER.info("pyspark script logger initialized")

# COMMAND ----------

args = toJStringArray(["-c","yaml_path","-o","result_path"])

sc._jvm.eu.semberal.dbstress.Main.main(args)

# COMMAND ----------

pjg.

# COMMAND ----------

from py4j.java_gateway import java_import
java_import(spark._sc._jvm, "eu.semberal.dbstress.*")

# COMMAND ----------

jg

# COMMAND ----------

jg.jvm.eu.semberal.dbstress

# COMMAND ----------

def toScala(x):
  return spark.sparkContext._jvm.scala.collection.JavaConverters.asScalaBufferConverter(x).asScala().toSeq()
def toJava(x):
  return spark.sparkContext._jvm.scala.collection.JavaConverters.seqAsJavaListConverter(x).asJava()

# COMMAND ----------

toJava(spark._jsparkSession.sharedState().externalCatalog().unwrapped().client().listDatabases("*"))

# COMMAND ----------

/Workspace/Repos/pavan.dendi@databricks.com/dbstress/bin/dbstress-assembly-0.0.0-SNAPSHOT.jar
bin/dbstress-assembly-0.0.0-SNAPSHOT.jar
