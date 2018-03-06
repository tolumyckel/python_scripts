#required libraries
import pandas as pd
import re

#using 1000 tweets fetched from twitter on trump and trudeau
trump = pd.read_csv("trump.csv")
trudeau = pd.read_csv("trudeau.csv")
#print trump['full_text']

# average number of times trump tweet per day
print trump.groupby(['each_day'])['full_text'].count().mean()

# average number of times trudeau tweet per day
print trudeau.groupby(['each_day'])['full_text'].count().mean()

#the week do trump tweet most frequently
print trump.groupby(['day'])['full_text'].count()

#the week do trudeau tweet most frequently
print trudeau.groupby(['day'])['full_text'].count()

#print type(trump['full_text'])
trump_fake = trump['full_text'].str.count(" fake ").sum()
trump_real = trump['full_text'].str.count(" real ").sum()
#trump_ratio = fake/real
print "Ratio of fake vs real in trump's tweets is ",trump_fake,":",trump_real

trudeau_fake = trudeau['full_text'].str.count(" fake ").sum()
trudeau_real = trudeau['full_text'].str.count(" real ").sum()
#trump_ratio = fake/real
print "Ratio of fake vs real in trump's tweets is ",trudeau_fake,":",trudeau_real
#print trump['full_text'].str.count("real").sum()

#print trump.groupby(['each_day'])trump['full_text'].str.count("trump").sum()

#ratio of the word 'good' vs 'bad' in their tweet
trump_good = trump['full_text'].str.count(" good ").sum()
trump_bad = trump['full_text'].str.count(" bad ").sum()
#trump_ratio = fake/real
print "Ratio of good vs bad in trump's tweets is ",trump_good,":",trump_bad

trudeau_good = trudeau['full_text'].str.count(" good ").sum()
trudeau_bad = trudeau['full_text'].str.count(" bad ").sum()


print "Ratio of good vs bad in trump's tweets is ",trudeau_good,":",trudeau_bad

print trump['full_text'].str.count(" u.s. ", flags=re.IGNORECASE).sum()
print trudeau['full_text'].str.count(" canada ", flags=re.IGNORECASE).sum()

#Number of times they use the word 'I'
print trump['full_text'].str.count(" I ").sum()
print trudeau['full_text'].str.count(" I ").sum()

#Number of times they use the word 'we'
print trump['full_text'].str.count(" we ").sum()
print trudeau['full_text'].str.count(" we ").sum()

#average number of words per tweet for trudeau
print trudeau['full_text'].str.split().apply(len).mean()

import dateutil
from datetime import date

newdate = trump['clean_created_at'].apply(dateutil.parser.parse, dayfirst=True)
trump['week'] = newdate.dt.week
#How many times a week does donald trump use his last name in his tweet tweets
trump['name_per_tweet'] = trump['full_text'].str.count(" trump ",flags=re.IGNORECASE)
#print trump['name_per_tweet']
print trump.groupby(['week'])['name_per_tweet'].sum().mean()
