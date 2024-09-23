import os
import sys
from time import time
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from the .env file
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

    # Read a sample to infer schema and check data types
    df = pd.read_csv(file_path, nrows=10)
    
    # Use dtype='object' to avoid type conflicts
    df_iter = pd.read_csv(file_path, iterator=True, chunksize=100000, dtype='object', low_memory=False)

    # Create the table
    df.head(0).to_sql(name=tb, con=engine, if_exists='replace')

    t_start = time()
    count = 0
    for batch in df_iter:
        count += 1
        
        # Clean data: Convert problematic columns to numeric if needed, coercing errors
        for col in batch.columns:
            try:
                batch[col] = pd.to_numeric(batch[col], errors='coerce')
            except ValueError:
                pass  # Skip conversion if not applicable
            
        print(f'Inserting batch {count}...')
        b_start = time()
        try:
            batch.to_sql(name=tb, con=engine, if_exists='append', index=False)
        except Exception as e:
            print(f"Error inserting batch {count}: {e}")
        b_end = time()
        print(f'Inserted! Time taken {b_end - b_start:10.3f} seconds.\n')

    t_end = time()
    print(f'Completed! Total time taken was {t_end - t_start:10.3f} seconds for {count} batches.')

if __name__ == '__main__':
    main()
