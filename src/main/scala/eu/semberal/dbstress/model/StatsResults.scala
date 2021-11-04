package eu.semberal.dbstress.model

import eu.semberal.dbstress.util.ModelExtensions._

case class StatsResults(
    count: Long,
    min: Option[Long],
    max: Option[Long],
    median: Option[Double],
    p90: Option[Double],
    p99: Option[Double],
    mean: Option[Double],
    stddev: Option[Double]
)

object StatsResults {
  def apply(l: List[Long]): StatsResults = {
    StatsResults(
      l.length,
      l.minimum,
      l.maximum,
      l.median,
      l.p90,
      l.p99,
      l.mean,
      l.stddev
    )
  }
}
