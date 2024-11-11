# ETL pipeline with Mage and GCP

## Requirements

### Docker

- Docker Installation:
    - Docker for Mac: 
        - Installation: [Install Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/)
    - Docker for Windows: 
        - Installation: [Install Docker Desktop on Windows](https://docs.docker.com/desktop/install/windows-install/)
- Ensure docker is running locally
- Make sure you create a `.env` file and fill out the environment variables

### Google Cloud Platform (GCP)

- Make sure you have a GCP account.
- Create a new project. [Creating and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
- Create a new bucket for your project in Google Cloud Storage. [Create buckets](https://cloud.google.com/storage/docs/creating-buckets)
- Create a new dataset and table in Google BigQuery. [Create and use tables](https://cloud.google.com/bigquery/docs/tables)
- Create a service account for your project and grant it with the role 'owner' (you can certainly do it in a more granular way and grant the minimal roles required for this project)
- Create a json key for your service account and put it in the same folder as the ``docker-compose.yml`` file. This will make sure that the service account key would be mounted to the path '/home/src/' within the container. 

## Instructions

1. Build images and run container with ``docker-compose.yml`` file

```bash
  docker-compose build
  docker-compose up -d
```

2. Navigate to 'localhost:6789' in your browser and you will be directed to Mage UI, where you can start building your pipelines!

![Mage UI](img/Mage UI.png)

3. I built two pipelines for this project which streamlined the entire ingestion, transformation and storage process.

- `api_load`: extract data from API, parse json format data to pandas dataframe and save partitioned parquet file to gcs. 
- `gcs_to_bq`:  ingest data from gcs and load data to BigQuery.

Detailed code chunks can be found in `data_exporters`, `data_loaders`, `transformaers` and `pipelines`.
