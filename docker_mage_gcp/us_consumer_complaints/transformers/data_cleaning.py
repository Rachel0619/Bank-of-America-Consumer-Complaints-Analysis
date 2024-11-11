import pandas as pd
import numpy as np

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):

    # we don't need 'company' column for this analysis because we are only dealing with BOA dataset
    df.columns = df.columns.str.lower() \
        .str.replace(' ', '_') \
        .str.replace('?', '', regex=False) \
        .str.replace('-', '_')
    df.drop(columns=['company'], axis=1, inplace=True)
    df.drop(columns=['consumer_disputed'], axis=1, inplace=True)
    df.rename(columns={
        'complaint_what_happened': 'consumer_complaint_narrative', "timely": "timely_response"}, 
        inplace=True)

    print("Finished Basic Formatting")

    # 2 Change data type

    df['date_received'] = pd.to_datetime(df.date_received, errors='coerce')
    df['date_sent_to_company'] = pd.to_datetime(df['date_sent_to_company'], errors='coerce')
    print("Finished changing data type")

    # 3 Impute missing values

    df.fillna({
        'sub_product': 'Unknown',
        'issue': 'Unknown',
        'sub_issue': 'Unknown',
        'consumer_complaint_narrative': 'No Narrative',
        'company_public_response': 'Unknown',
        'state': 'Unknown',
        'zip_code': 'Unknown',
        'tags': 'No Tags',
        'consumer_consent_provided': 'No Consent Provided',
        'consumer_disputed': 'Unknown'
    }, inplace=True)

    # 4 Feature Engineering

    # df['year_month'] = df['date_received'].dt.strftime('%Y-%m')
    df['timely_response'] = df['timely_response'].map({'Yes': 1, 'No': 0})
    print("Finished feature engineering")

    # print(df.info())

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert not output.isna().any().any(), 'We still have missing values'
