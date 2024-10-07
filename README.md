# Bank of America Consumer Complaints Analysis 

## 📊 Project Background 
This analysis focuses on consumer complaints filed against Bank of America (BOA), using data sourced from the Consumer Complaint Database provided by the Consumer Financial Protection Bureau (CFPB). The dataset contains information on a wide variety of consumer complaints related to financial products and services, including details such as the product, issue, state, and demographic tags. For this analysis, I filtered the dataset to focus exclusively on complaints related to Bank of America, rather than analyzing the entire database. The timeframe of this analysis covers complaints received between 2018-01-01 and 2024-09-25.

The objective of the analysis is to explore both the distribution and trends of complaints by product/sub-product, issue/sub-issue, and demographic group, providing insights into areas where Bank of America may need to improve customer service, operational efficiency, and product offerings. I wrote PostgreSQL queries to examine the proportion and distribution of complaints, identifying which products and issues are most common. Additionally, I created a Tableau dashboard to visualize the trends over time. 

Insights and recommendations are provided on the following key areas:

- **Category 1: Product Analysis**
- **Category 2: Issue Analysis**
- **Category 3: Demographical Analysis** 

The jupyter notebook for EDA analysis can be found [here](https://github.com/Rachel0619/US-Consumer-Finance-Complaints-Analysis/blob/main/EDA.ipynb).
The jupyter notebook for data cleaning and wrangling can be found [here](https://github.com/Rachel0619/US-Consumer-Finance-Complaints-Analysis/blob/main/transformation.ipynb).
The python script that load data to postgres database can be found [here](https://github.com/Rachel0619/US-Consumer-Finance-Complaints-Analysis/blob/main/data_loading_csv.py).
SQL queries that answer various business questions can be found [here](https://github.com/Rachel0619/US-Consumer-Finance-Complaints-Analysis/blob/main/analysis_sql_query.ipynb).
An interactive Tableau dashboard used to report and explore sales trends can be found [here](https://public.tableau.com/app/profile/rachel.li3670/viz/consumerfinancecomplaints/Trend).

## 🗂️ Dataset Overview and Field Descriptions

You will get a full picture of the database this project works on by examining this [field refernce](https://cfpb.github.io/api/ccdb/fields.html). 


This database contains a total of 17 fields (I dropped the "company" column because we are only working with Bank of America data here. I also dropped the "Consumer disputed?" here because all values for this field are missing):

- Text (Categorical and Descriptive): 12 fields, including fields like Product, Issue, Company public response, Consumer complaint narrative, and Tags. Many of these fields are categorical, while some like Consumer complaint narrative contain substantial text. 
- Date & Time: 2 fields, including Date received and Date sent to company. These fields allow for temporal analysis, such as identifying complaint trends over time.
- Numeric: 1 field, Complaint ID, which is a unique identifier for each complaint.
- Boolean: 2 fields, including Timely response?, Consumer consent provided?, which are binary in nature (yes/no). 

Given the heavy presence of text fields, especially the `Consumer complaint narrative`, this database lends itself well to NLP techniques to extract insights such as common themes, sentiment analysis, or complaint categorization. 

## 🔍 Overview of Findings

The analysis reveals that checking and savings accounts are the most frequent source of complaints, with checking accounts alone accounting for a significant portion of consumer dissatisfaction. Issues around account management and fund transactions, particularly deposits and withdrawals, are also common themes in the complaints. On a demographic level, Washington, D.C. had the highest number of complaints per 1000 people in 2023, while Older Americans and Servicemembers represented key groups that require tailored attention to address their unique financial needs. These findings highlight several areas for improvement in Bank of America's products and services, with particular emphasis on customer service and operational efficiency in core banking functions.

[Visualization, including a graph of overall trends or snapshot of a dashboard]


## 📈 Insights Deep Dive
### Product Analysis:

- The "Checking or savings account" product category generated the highest number of complaints, representing 39.63% of the total. This indicates that core banking services are a significant source of dissatisfaction for Bank of America customers.

- Checking accounts specifically account for 84% of the complaints within this category. This suggests that operational and service-related issues in checking accounts—such as accessibility, fees, and transaction management—are key areas for improvement. Addressing these issues could significantly reduce the volume of complaints.

### Issue Analysis:

- The most common issue faced by Bank of America customers is "Managing an account", which accounts for 24.06% of all complaints. This highlights potential service gaps in areas such as account maintenance, customer support, and online banking functionality.

- A deeper look at sub-issues reveals that "Deposits and withdrawals" are a major pain point, representing 8.93% of all complaints. This suggests that Bank of America may need to focus on improving the efficiency and accuracy of handling customer funds, particularly in deposit and withdrawal transactions.


### Demographical Analysis:

- Washington, D.C. (DC) leads the ranking of complaints per 1000 people in 2023, showing a higher complaint rate when adjusted for population. This could indicate a region-specific issue or higher consumer awareness of financial protections in DC, warranting further investigation into the underlying causes of dissatisfaction in this area.

- Older Americans represent 7.43% of total complaints, while Servicemembers account for 5.52%. These two groups, though smaller in volume, likely face unique challenges, and tailored services or support mechanisms may be required to address their specific needs. Understanding and resolving their issues could help Bank of America better serve these important customer segments.


## 💡 Recommendations:

Based on the insights and findings above, we would recommend the [stakeholder team] to consider the following: 

* Specific observation that is related to a recommended action. **Recommendation or general guidance based on this observation.**
  
* Specific observation that is related to a recommended action. **Recommendation or general guidance based on this observation.**
  
* Specific observation that is related to a recommended action. **Recommendation or general guidance based on this observation.**
  
* Specific observation that is related to a recommended action. **Recommendation or general guidance based on this observation.**
  
* Specific observation that is related to a recommended action. **Recommendation or general guidance based on this observation.**
  


## ⚠️ Assumptions and Caveats:

Throughout the analysis, multiple assumptions were made to manage challenges with the data. These assumptions and caveats are noted below:

* Assumption 1 (ex: missing country records were for customers based in the US, and were re-coded to be US citizens)
  
* Assumption 1 (ex: data for December 2021 was missing - this was imputed using a combination of historical trends and December 2020 data)
  
* Assumption 1 (ex: because 3% of the refund date column contained non-sensical dates, these were excluded from the analysis)

## 🛠️ Developer Guide

I used docker container to run my analysis. To replicate the workflow, run the following steps:

Make sure your docker daemon is running before starting.

```
docker-compose build
docker-compose up -d
```

run `docker ps` to make sure that container for postgres and pgadmin are running, then navigate to 'localhost:8080' to open pgadmin GUI and login using the environment variable stored in `.env` file.

run `data_loading_csv.py` to load data into postgres database.