import requests
import pandas as pd

url = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/"

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
    file_path = f"../data/raw/BOA_consumer_complaints_{params['date_received_min']}_to_{params['date_received_max']}.csv"
    df.to_csv(file_path, index=False)
    
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")






