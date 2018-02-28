
# coding: utf-8

# In[32]:


import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'W1cR90n5qoozBow9HTyNQo9D1'
consumer_secret= 'gjEce5QOdASqlEQY34EV33brCHrqFXN4GCni5FSbAJMgarqvgA'

access_token='726938717630255104-qXADtJNB0OXMUaS4FpIL2o2vDs1Usdf'
access_token_secret='lo7Nmr7dnIIftfeL2swX35oVXjJdYMaTNbQYQLvGPAfji'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself

data = []
for tweet in public_tweets:
    if analysis.sentiment[0] > 0.0:
        dic = {'text':tweet.text,'polarity':analysis.sentiment[0],'subjectivity':analysis.sentiment[1],'sentiment':'positive'}
    else:
        dic = {'text':tweet.text,'polarity':analysis.sentiment[0],'subjectivity':analysis.sentiment[1],'sentiment':'negative'}

    data.append(dic)
    print(tweet.text)
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
    


# In[33]:


data 


# In[34]:


import csv


# In[35]:


with open('output.csv',"w") as outfile:
    fieldnames = ('polarity','sentiment','subjectivity','text')
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)


# In[36]:


import pandas as pd


# In[37]:


df = pd.read_csv('output.csv')


# In[39]:


df.tail()

