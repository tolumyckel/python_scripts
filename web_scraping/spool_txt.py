import tweepy
import json, csv, time
import requests, types
from requests.exceptions import RequestException
consumer_key = "TIWTTER_CONSUMER_KEY"
consumer_secret = "TWITTER_SECRET_KEY"
access_token = "TWITTER_ACCESS_TOKEN"
access_token_secret = "TWITTER_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

google_api = "GOOGLE_API_KEY"
cx = "SEARCH_ENGINE_KEY"

search_base = "https://www.googleapis.com/customsearch/v1"

the_list = []
url_list = []
with open('handle.txt', 'r+') as txtfile:
    data = txtfile.readlines()
    rows = data
    i = 0
    start = time.time()
    for row in rows:
        print "Starting ", i,"th iterion"
        if i != 0:
            result = row.rstrip()
            try:
                output = api.get_user(result)
                if type(output._json["url"]) is not types.NoneType:
                    the_list.append({
                            "Name": output._json["name"].encode("utf-8"),
                            "ScreenName": output._json["screen_name"].encode("utf-8"),
                            "Url":output._json["url"].encode("utf-8")
                            })
                    with open("twitter_handle_from_text.json","w+") as jsonFile1:
                        json.dump(the_list, jsonFile1, indent=4)
                    print len(the_list), " handle information saved from twitter"
                    with open('twitter_handle_from_text.csv', 'w+') as twitter_data:

                    # create the csv writer object

                        csvwriter = csv.writer(twitter_data)

                        count = 0
                        for twitter in the_list:

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

                else:
                    search_query = "?q="+result+"&cx="+cx+"&num=3&fields=items&key="+google_api
                    search_url = search_base+search_query
                    try:
                        response = requests.get(search_url)
                        if response.ok:
                            get_response = response
                            response.close()
                            res_json = json.loads(get_response.content)
                            if len(res_json["items"]) == 3:
                                url_list.append({"Name": output._json["name"],
                                    "ScreenName": output._json["screen_name"],
                                    "Possible_url1": res_json["items"][0]["link"].encode("utf-8"),
                                    "Possible_url2": res_json["items"][1]["link"].encode("utf-8"),
                                    "Possible_url3": res_json["items"][2]["link"].encode("utf-8")
                                                })
                            else:
                                url_list.append({"Name": output._json["name"],
                                    "ScreenName": output._json["screen_name"],
                                    "Possible_url1": res_json["items"][0]["link"].encode("utf-8"),
                                    "Possible_url2": "",
                                    "Possible_url3": ""
                                                })
                            with open("twitter_handle2_from_text.json","w+") as jsonFile2:
                                json.dump(url_list, jsonFile2, indent=4)
                            print len(url_list), " handle information saved from google"
                            with open('twitter_handle2_from_text.csv', 'w+') as twitter_data2:

                            # create the csv writer object

                                csvwriter2 = csv.writer(twitter_data2)

                                count = 0
                                for twitter2 in url_list:

                                      if count == 0:

                                             header2 = twitter2.keys()

                                             csvwriter2.writerow(header2)

                                             count += 1
                                      newList2 = []
                                      for twit in twitter2.values():
                                          #print type(twit)
                                          if type(twit) is types.UnicodeType:
                                              newList2.append(twit.encode("utf-8"))
                                          else:
                                              newList2.append(twit)
                                      csvwriter2.writerow(newList2)

                        else:
                            pass
                            print "Not able to get data due to", response.status_code
                    except RequestException as e:
                        pass
                        print e
            except tweepy.TweepError as e:
                pass
                print e.reason, " for ", result
            end = time.time()
            print "Time taken to complete", i,"th iteration: ",end-start,"seconds"
            print "Delay for 10 seconds"
            time.sleep(10)
        else:
            pass
        i += 1
    final = time.time()
    total = final - start
    print "Total time taken ", total/3600, "hours!!!"

    
print "Done!!!"
