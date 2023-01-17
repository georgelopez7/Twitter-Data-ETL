# Twitter Data ETL

![MicrosoftTeams-image_1](https://user-images.githubusercontent.com/71076769/212990225-eeec3993-703b-4c33-ac82-797cb7449089.png)

> An ETL (Extract, Transform and Load) pipeline that utilizes the Twitter API to gather the number of likes and retweets of OpenAI's tweets and loads the data into pdAdmin.

---

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
    
    -  [Technologies & Softwares](#technologies)
- [Database](#database)

    -  [Data Example](#data-example) 
- [Author Info](#author-info)

---

## Description

This project is an ETL (Extract, Transform and Load) pipeline that utilizes the Twitter API and the Tweepy package in Python to gather tweets from the OpenAI twitter account. The tweets are then parsed to extract 
number of likes and retweets for each tweet. These attributes are then transformed and loaded into Pandas dataframes before being loaded into a series of tables in pgAdmin. 

To load the data, the project makes use of SQLAlchemy and psycopg2, which is a Python library that provides an ORM (Object-Relational Mapping) API for interacting with PostgreSQL (pgAdmin). 

The primary goal of the project is to collect data on the engagement of the OpenAI twitter account and understand how the tweets are being received by the audience using ETL approach. The collected data is used to analyze the performance of the tweets over time and identify patterns in engagement. 

### Technologies and Softwares

- Python
    - **tweepy** package
    
        Used to interact with the Twitter API and collect the tweets.
    - **pandas** package

        Used to store the data before it is loaded in pgAdmin.
    - **SQLAlchemy & psycopg2** package

        Used to connect and interact with a PostgreSQL database (pgAdmin).

- pgAdmin
    
    Used store the collected data from the Twitter API.

- SQL

    Used in pgAdmin to query the database.

[Back To The Top](#twitter-data-etl)

---

## Database

Below you can see the ER (Entity Relationship) Diagram of the database in pgAdmin:

![ER_Diagram_1](https://user-images.githubusercontent.com/71076769/212990124-84934041-2af0-4608-9f78-6f57c71d1cb5.png)


### Data Example

After running the following SQL command we retrieve the table shown below.

```
SELECT  
    tweets.id as tweet_id,
    date as tweet date,
    text as tweet_content,
    likes,
    retweets
FROM tweets
JOIN dates on tweets.id = dates.id
JOIN stats on tweets.id = stats.id
LIMIT 5
```

tweet_id | tweet_date | tweet_content | likes | retweets 
--- | --- | --- | --- |--- 
1615160228366147600 | 2023-01-17 01:33:01+00 | We've learned a lot from the ChatGPT research prev...|8741 | 1371 
1613182128661069800 | 2023-01-11 14:32:45+00 | We're publishing a report, co-authored with @CSETG... | 2002| 472 
1603466863370854400 | 2022-12-15 19:07:45+00 | Our new embedding model is significantly more capa... | 2716| 473
1598014522098208800 | 2022-11-30 18:02:06+00 | Try talking with ChatGPT, our new AI system which... | 13031| 3421
1588214604798181400 | 2022-11-03 17:00:44+00 | Weâ€™ve just launched the DALLÂ·E API so developer... | 3700| 717 

[Back To The Top](#twitter-data-etl)

---

## Authors Info

LinkedIn - [George Lopez](https://www.linkedin.com/in/george-benjamin-lopez/)
LinkedIn - [Jasmine Albert](https://www.linkedin.com/in/jasmine-albert-99029b207/)
LinkedIn - [Matias Sanchez Wilson](https://www.linkedin.com/in/matiassanchezwilson/)
LinkedIn - [Asfia Hossoin](https://www.linkedin.com/in/asfia-hossoin-9521b6243/)


[Back To The Top](#twitter-data-etl)
