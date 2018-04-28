import json
import requests
import urllib
import youtube_info
import time

def query_youtube():
        api_url = youtube_info.api_base + youtube_info.api_querystring + youtube_info.api_token

        response = requests.get(api_url)

        result_json = json.loads(response.content)
        return result_json



def get_comments(result_json, result):
        for res in result_json["items"]:
                
                result.append(res["snippet"]["topLevelComment"]["snippet"])
                

        print json.dumps(result, indent=4)

def run_sentiment_on_comments(result_json, result):
        for res in result_json["items"]:
                
                resu = urllib.quote_plus(res["snippet"]["topLevelComment"]["snippet"]["textDisplay"].encode("utf-8"))
                
                senti_data = requests.post("http://text-processing.com/api/sentiment/", data="text="+resu)
                
                sentiment = json.loads(senti_data.content)
                if sentiment["label"].encode("utf-8") == "pos":
                        result.append({"comment": res["snippet"]["topLevelComment"]["snippet"]["textDisplay"].encode("utf-8"),
                                "negative_value": sentiment["probability"]["neg"],
                                "positive_value": sentiment["probability"]["pos"],
                                "neutral_value": sentiment["probability"]["neutral"],
                                "sentiment": "positive"})
                elif sentiment["label"].encode("utf-8") == "neg":
                        result.append({"comment": res["snippet"]["topLevelComment"]["snippet"]["textDisplay"].encode("utf-8"),
                                "negative_value": sentiment["probability"]["neg"],
                                "positive_value": sentiment["probability"]["pos"],
                                "neutral_value": sentiment["probability"]["neutral"],
                                "sentiment": "negative"})
                else:
                        result.append({"comment": res["snippet"]["topLevelComment"]["snippet"]["textDisplay"].encode("utf-8"),
                                "negative_value": sentiment["probability"]["neg"],
                                "positive_value": sentiment["probability"]["pos"],
                                "neutral_value": sentiment["probability"]["neutral"],
                                "sentiment": sentiment["label"].encode("utf-8")})
                print json.dumps(result, indent=4)

                #To avoid overloading the sentiment api service, set sleep the process for 30 seconds
                time.sleep(30)

        print json.dumps(result, indent=4)

if __name__ == '__main__':
        output = query_youtube()
        result1 = []
        result2 =[]
        get_comments(output,result1)
        print "Sentiment"
        run_sentiment_on_comments(output,result2)
