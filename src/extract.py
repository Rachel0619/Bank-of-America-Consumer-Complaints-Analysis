import pandas as pd
import numpy as np

# Extract the census data

df_census = pd.read_csv("../data/raw/census_population_by_state.csv")

# convert columns names to integers

df_census.columns = [int(col) if col.isdigit() else col for col in df_census.columns]

# remove the "." in front of the states name

df_census["State"] = df_census["State"].str.lstrip(".")

# convert data types for popluation values to int

for col in range(2020, 2024):
    df_census[col] = df_census[col].str.replace(',', '')  # Remove commas
    df_census[col] = df_census[col].astype(int)

# convert the table to long format to integrate year into one column
df_census_long = pd.melt(df_census, id_vars=['State'], value_vars=[2020, 2021, 2022, 2023],
                  var_name='Year', value_name='Population')

state_to_abbreviation = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    'District of Columbia': 'DC'
}

# Replace the 'State' column with the abbreviations in place
df_census_long['State'] = df_census_long['State'].map(state_to_abbreviation)

# change all column names to lower cases
df_census_long.columns = [x.lower() for x in df_census_long.columns]

# Save results
df_census_long.to_csv("../data/processed/census_population_by_state.csv", index=False)
print("Saved census data after processing")