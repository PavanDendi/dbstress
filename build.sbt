import sbt.Keys._

val dependencies = Seq(
  "com.typesafe.akka" %% "akka-actor" % Versions.akka,
  "com.typesafe.akka" %% "akka-slf4j" % Versions.akka,
  "com.typesafe.scala-logging" %% "scala-logging" % Versions.scalaLogging % "provided",
  "org.yaml" % "snakeyaml" % Versions.snakeYaml % "provided",
  "com.github.pathikrit" %% "better-files" % Versions.betterFiles,
  "com.github.tototoshi" %% "scala-csv" % Versions.scalaCsv,
  "org.apache.commons" % "commons-math3" % Versions.commonsMath % "provided",
  "com.github.scopt" %% "scopt" % Versions.scopt,
  "org.apache.commons" % "commons-lang3" % Versions.commonsLang3 % "provided",
  "ch.qos.logback" % "logback-classic" % Versions.logbackClassic,
  "com.typesafe.akka" %% "akka-testkit" % Versions.akka % "test, it, provided",
  "org.scalatest" %% "scalatest" % Versions.scalatest % "test, it, provided",
  "org.scalatest" %% "scalatest-flatspec" % Versions.scalatest % "test, it, provided",
  "org.postgresql" % "postgresql" % Versions.postgres % "test, it, provided"
)

// resolvers += "S3" at "s3://db-field-eng-mvn/"

lazy val dbstresss = (project in file("."))
  .enablePlugins(PackPlugin)
  .settings(
    organization := "com.databricks.labs",
    name := "sqlstorm",
    version := sys.env.getOrElse("SQLSTORM_VERSION", "0.0.0-SNAPSHOT"),
    scalaVersion := Versions.scala,
    publishMavenStyle := true,
    publishTo := {
        val s3root = "s3://db-field-eng-mvn/"
        if (isSnapshot.value)
           // Some("S3" at s3root + "snapshot/")
            Some("S3" at s3root + "snapshot/")
        else
            Some("S3" at s3root + "release/")
    },
    scalacOptions ++= Seq(
      "-target:jvm-1.8",
      "-unchecked",
      "-deprecation",
      "-feature",
      "-Xfatal-warnings",
      "-Ywarn-unused:imports"
    ),
    awsProfile := Some("aws-field-eng_databricks-power-user"),
    s3region := Region("us-west-1")  
)
  .configs(IntegrationTest)
  .settings(Defaults.itSettings: _*)
  .settings(libraryDependencies ++= dependencies: _*)
  .settings(packMain := Map("sqlstorm" -> "eu.semberal.dbstress.Main"))
  .settings(
    inConfig(IntegrationTest)(
      org.scalafmt.sbt.ScalafmtPlugin.scalafmtConfigSettings
    )
  )
