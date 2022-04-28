cluter json config:

{
    "new_cluster": {
    "spark_version": "10.4.x-scala2.12",
    "node_type_id": "r3.xlarge",
    "aws_attributes": {
      "availability": "ON_DEMAND"
    },
    "num_workers": 10,
    "policy_id": "ABCD000000000000"
    },
    "num_workers": 0,
    "cluster_name": "test-clusters-api",
    "spark_version": "10.4.x-scala2.12",
    "spark_conf": {
        "spark.databricks.python.defaultPythonRepl": "ipykernel",
        "spark.master": "local[*, 4]",
        "spark.databricks.cluster.profile": "singleNode"
    },
    "aws_attributes": {
        "first_on_demand": 1,
        "availability": "SPOT_WITH_FALLBACK",
        "zone_id": "auto",
        "instance_profile_arn": "arn:aws:iam::997819012307:instance-profile/shard-demo-s3-access",
        "spot_bid_price_percent": 100,
        "ebs_volume_type": "GENERAL_PURPOSE_SSD",
        "ebs_volume_count": 1,
        "ebs_volume_size": 100
    },
    "node_type_id": "m5a.large",
    "driver_node_type_id": "m5a.large",
    "ssh_public_keys": [],
    "custom_tags": {
        "ResourceClass": "SingleNode"
    },
    "spark_env_vars": {},
    "autotermination_minutes": 30,
    "enable_elastic_disk": true,
    <!-- "cluster_source": "UI", -->
    "init_scripts": [],
    "policy_id": "E060384AFC00043E",
    <!-- "cluster_id": "0414-071034-r3kae1ar" -->
}

{
  "run_name": "my spark task",
  "new_cluster": {
    "spark_version": "10.4.x-scala2.12",
    "node_type_id": "r3.xlarge",
    "aws_attributes": {
      "availability": "ON_DEMAND"
    },
    "num_workers": 10,
    "policy_id": "ABCD000000000000"
  },
  "libraries": [
    {
      "jar": "dbfs:/my-jar.jar"
    },
    {
      "maven": {
        "coordinates": "org.jsoup:jsoup:1.7.2"
      }
    }
  ],
  "spark_jar_task": {
    "main_class_name": "com.databricks.ComputeModels"
  }
}

{
  "cluster_id": "10201-my-cluster",
  "libraries": [
    {
      "jar": "dbfs:/mnt/libraries/library.jar"
    },
    {
      "egg": "dbfs:/mnt/libraries/library.egg"
    },
    {
      "whl": "dbfs:/mnt/libraries/mlflow-0.0.1.dev0-py2-none-any.whl"
    },
    {
      "whl": "dbfs:/mnt/libraries/wheel-libraries.wheelhouse.zip"
    },
    {
      "maven": {
        "coordinates": "org.jsoup:jsoup:1.7.2",
        "exclusions": ["slf4j:slf4j"]
      }
    },
    {
      "pypi": {
        "package": "simplejson",
        "repo": "https://my-pypi-mirror.com"
      }
    },
    {
      "cran": {
        "package": "ada",
        "repo": "https://cran.us.r-project.org"
      }
    }
  ]
}