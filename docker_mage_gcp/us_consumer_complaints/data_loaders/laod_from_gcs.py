from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path
import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/swift-kiln-441121-a4-bcd35c6bb038.json"

@data_loader
def load_from_google_cloud_storage(*args, **kwargs):
    bucket_name = 'bkt_landing_zone_boa'
    folder_name = 'complaints_data'
    root_path = f'{bucket_name}/{folder_name}'

    gcs = pa.fs.GcsFileSystem()
    df_pq = pq.ParquetDataset(root_path, filesystem=gcs)
    df = df_pq.read_pandas().to_pandas()
    # print(df.shape)
        
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
