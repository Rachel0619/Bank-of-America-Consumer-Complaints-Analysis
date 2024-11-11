import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/"
    response = requests.get(url)

    # Define parameters
    params = {
        "company": "BANK OF AMERICA, NATIONAL ASSOCIATION",  # Specify BOA
        "date_received_min": "2024-01-01", 
        "date_received_max": "2024-08-31", 
        "format": "json",  # Response format
        "size": 10,  # Limit to 10 entries; adjust as needed
        "sort": "created_date_desc"  # Sort by the most recent created date
    }

    # Send GET request
    response = requests.get(url, params=params)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()
        print("Data retrieved successfully!")
        complaints = []
        
        # Iterate over each complaint entry in the list
        for complaint in data:
            complaint_details = complaint.get('_source', {})
            complaints.append(complaint_details)
        
        df = pd.DataFrame(complaints)
        print(f"Retrived {df.shape[0]} records from {params['date_received_min']} to {params['date_received_max']}")
        
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
    
    print(df.loc[0, 'date_sent_to_company'])
    
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
