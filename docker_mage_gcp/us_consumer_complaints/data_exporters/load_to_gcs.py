from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path
import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/swift-kiln-441121-a4-bcd35c6bb038.json"
bucket_name = 'bkt_landing_zone_boa'
project_id = 'swift-kiln-441121-a4'
table_name = "complaints_data"
root_path = f"{bucket_name}/{table_name}"

@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:

    df['date_received_year'] = df['date_received'].dt.year
    df['date_received_month'] = df['date_received'].dt.month

    table = pa.Table.from_pandas(df)
    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path = root_path,
        partition_cols=['date_received_year', 'date_received_month'],
        filesystem=gcs
    )
