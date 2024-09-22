#Cleaned up version of data-loading.ipynb
import argparse, os, sys
from time import time
import pandas as pd 
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def main():
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')
    db = os.getenv('POSTGRES_DBNAME')
    tb = 'complaints'
    file_path = os.path.join(os.getcwd(), 'consumer_complaints.csv') 
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit()

    print(f'Loading {file_path} ...\n')

    # Create SQL engine
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Read the CSV file
    df = pd.read_csv(file_path, nrows=10)  # Read a small sample to infer schema
    df_iter = pd.read_csv(file_path, iterator=True, chunksize=100000)

    # Create the table
    df.head(0).to_sql(name=tb, con=engine, if_exists='replace')

    t_start = time()
    count = 0
    for batch in df_iter:
        count += 1
        print(f'Inserting batch {count}...')
        b_start = time()
        batch.to_sql(name=tb, con=engine, if_exists='append')
        b_end = time()
        print(f'Inserted! Time taken {b_end - b_start:10.3f} seconds.\n')

    t_end = time()
    print(f'Completed! Total time taken was {t_end - t_start:10.3f} seconds for {count} batches.')

if __name__ == '__main__':
    main()