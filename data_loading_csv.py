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
    file_path = os.path.join(os.getcwd(), 'data/complaints_transformed.csv') 
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit()

    print(f'Loading {file_path} ...\n')

    # Create SQL engine
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df = pd.read_csv(file_path)

    t_start = time()

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}') 
    table_name = "complaints"

    df.to_sql(table_name, engine, if_exists='replace', index=False)

    t_end = time()
    print(f'Completed! Total time taken was {t_end - t_start:10.3f} seconds')

if __name__ == '__main__':
    main()
