from pandas.core.frame import DataFrame as PandasDataFrame
from polars.dataframe.frame import DataFrame as PolarsDataFrame
from pyspark.sql.dataframe import DataFrame as SparkDataFrame
from dask.dataframe.core import DataFrame as DaskDataFrame
from modin.pandas.dataframe import DataFrame as ModinDataFrame


class DataFrame:
    """Generic (bear-agnostic) DataFrame type"""

    def __init__(self, df: PolarsDataFrame | PandasDataFrame | SparkDataFrame | DaskDataFrame | ModinDataFrame): ...
