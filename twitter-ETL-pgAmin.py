# Twitter ETL Pipeline
# -----------------------------------------------------------------------
import tweepy
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
# -----------------------------------------------------------------------
# Login Credentials for the Twitter API
 
# Set up API credentials for Twitter API
consumer_key = 'Add-Twitter-Consumer-Key-Here'
consumer_secret = 'Add-Twitter-Consumer-Secret-Here'
access_token = 'Add-Twitter-Access-Token-Here'
access_token_secret = 'Add-Twitter-Access-Token-Secret-Here'

# Authenticate using the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# -----------------------------------------------------------------------
# Get the tweets from the OpenAI Twitter account
tweets = api.user_timeline(screen_name='openai', count=200)

# Create lists to store the data
ids = []
texts = []
dates = []
likes = []
retweets = []

# Iterate over the tweets and store the data
for tweet in tweets:
    ids.append(tweet.id)
    texts.append(tweet.text)
    dates.append(tweet.created_at)
    likes.append(tweet.favorite_count)
    retweets.append(tweet.retweet_count)

# Create dataframes to store the data
df_texts = pd.DataFrame({'id': ids, 'text': texts})
df_dates = pd.DataFrame({'id': ids, 'date': dates})
df_likes_retweets = pd.DataFrame({'id': ids, 'likes': likes, 'retweets': retweets})
# -----------------------------------------------------------------------
# Importing the dataframes into pgAdmin

# Credentials for pgAdmin
# Username
ptgrs_username = 'Add-PostgreSQL-Username-Here'
# Password
ptgrs_pwd = 'Add-PostgreSQL-Password-Here'
# Host
ptgrs_host = 'Add-PostgreSQL-Host-Here'
# Port
ptgrs_port = 'Add-PostgreSQL-Port-Here'
# Database Name
ptgrs_database = 'Add-PostgreSQL-Database-Name-Here'
# -----------------------------------------------------------------------
# Prevent duplicate Data
# The try statement ensures data is not replicated in the database
try:
    # Making the connection to postgres using psycopg2 to query the database
    conn = psycopg2.connect(
        host=ptgrs_host,
        database=ptgrs_database,
        user=ptgrs_username,
        password=ptgrs_pwd,
        port = ptgrs_port
    )

    # Create a cursor
    cur = conn.cursor()

    # Execute a SELECT statement to retrieves the ids of the column
    cur.execute("SELECT id FROM dates")

    # Fetch all the rows into a list
    rows = cur.fetchall()

    for iden in df_dates['id'].to_list():
        for row in rows:
            if iden == row[0]:
                df_dates = df_dates.loc[df_dates['id'] != iden, :]
 
    # Execute a SELECT statement to retrieves the ids of the column
    cur.execute("SELECT id FROM retweets")

    # Fetch all the rows into a list
    rows = cur.fetchall()

    for iden in df_likes_retweets['id'].to_list():
        for row in rows:
            if iden == row[0]:
                df_likes_retweets = df_likes_retweets.loc[df_likes_retweets['id'] != iden, :]

    # Execute a SELECT statement to retrieves the ids of the column
    cur.execute("SELECT id FROM texts")

    # Fetch all the rows into a list
    rows = cur.fetchall()

    print(len(df_texts)) # feedback to ensure it is working

    for iden in df_texts['id'].to_list():
        for row in rows:
            if iden == row[0]:
                df_texts = df_texts.loc[df_texts['id'] != iden, :]

    print(len(df_texts))
    # -----------------------------------------------------------------------
    # Close the cursor and connection
    cur.close()
    conn.close()
# If there is no table that exists we move to this except statement
except: 
    pass

# Creating the engine to connect to postgres in order to alter tables
engine = create_engine(f'postgresql+psycopg2://{ptgrs_username}:{ptgrs_pwd}@{ptgrs_host}:{ptgrs_port}/{ptgrs_database}')

# Insert the Text DataFrame into --> tweets table
df_texts.to_sql('texts', engine, if_exists='append', index=False)
# Insert the Stats DataFrame into --> stats table
df_likes_retweets.to_sql('retweets', engine, if_exists='append', index=False)
# Insert the Dates DataFrame into --> dates table
df_dates.to_sql('dates', engine, if_exists='append', index=False)
# -----------------------------------------------------------------------
# Check the data in pgAdmin!



