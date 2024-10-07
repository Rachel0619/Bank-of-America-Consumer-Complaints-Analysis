import os
import sys
from time import time
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def load_data_to_db(file_path, table_name, engine):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit()

    print(f'Loading {file_path} into table {table_name}...\n')

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    t_start = time()

    # Load DataFrame to the SQL table
    df.to_sql(table_name, engine, if_exists='replace', index=False)

    t_end = time()
    print(f'Completed loading {table_name}! Total time taken was {t_end - t_start:10.3f} seconds')

def main():
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')
    db = os.getenv('POSTGRES_DBNAME')

    # Create SQL engine
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Load the complaints file
    complaints_file_path = os.path.join(os.getcwd(), 'data/processed/complaints_transformed_2.csv')
    load_data_to_db(complaints_file_path, 'complaints', engine)

    # Load the census population file
    census_file_path = os.path.join(os.getcwd(), 'data/processed/census_population_by_state.csv')
    load_data_to_db(census_file_path, 'population_state', engine)

if __name__ == '__main__':
    main()

