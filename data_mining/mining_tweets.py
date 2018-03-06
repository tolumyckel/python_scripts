#Required libraries
import tweepy
import json
import csv
import types

#authentication parameters
consumer_key = "xxxxxx"
consumer_secret = "xxxxxx"
access_token = "xxxxxxx"
access_token_secret = "xxxxxxx"

#authenticating parameters using tweepy methods
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

#fetch 1000 tweets with full text for a user named 'twitter_handle'
result1 = tweepy.Cursor(api.user_timeline,id = "twitter_handle",tweet_mode="extended").items(1000)
lists = []
for tweet1 in result1:
    lists.append(tweet1._json)

#wirte tweets in json format to json file
with open("file.json","w+") as jsonFile1:
        json.dump(lists,jsonFile1)
print len(lists)




# open a file for writing

with open('file.csv', 'w+') as twitter_data:

# create the csv writer object

    csvwriter = csv.writer(twitter_data)

    count = 0
    for twitter in lists:

          if count == 0:

                 header = twitter.keys()

                 csvwriter.writerow(header)

                 count += 1
          newList = []
          for twit in twitter.values():
              #print type(twit)
              if type(twit) is types.UnicodeType:
                  newList.append(twit.encode("utf-8"))
              else:
                  newList.append(twit)
          csvwriter.writerow(newList)
          #csvwriter.writerow(twitter.values().encode("utf-8"))

    
    print "Success!!!"
