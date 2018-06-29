import requests
import json

api_url1 = "https://s3.amazonaws.com/misc-file-snack/MOCK_SNACKER_DATA.json"
api_url2 = "https://desknibbles.ca/products.json?limit=250"

response1 = requests.get(api_url1)
response2 = requests.get(api_url2)

result1 = json.loads(response1.content.decode("utf-8"))
result2 = json.loads(response2.content.decode("utf-8"))

snack_list = []

#for res1 in result1:
    
 #   for i in range(len(result2["products"])):
        
  #      if(res1["fave_snack"] == result2["products"][i]["title"]):
   #         print(res1["email"]+ " " + result2["products"][i]["title"] + " "+ result2["products"][i]["variants"][0]["price"])
            #if(result2["products"][i]["title"] in snack_list):
             #   total += result2["products"][i]["variants"][0]["price"]
              #  continue
            #else:
    #        snack_list.append(result2["products"][i]["title"])
            #print(res1["email"]+ " " + result2["products"][i]["title"] + " "+ result2["products"][i]["variants"][0]["price"])
#print(snack_list)
#snacks = {j:snack_list.count(j) for j in snack_list}

#print(snacks)

def question_one(snackers,store):
    print("******")
    print("Question 1")
    print("******")
    print("Real Stocked Snacks with their number of occurence in a list")
    for snacker in snackers:
    
        for i in range(len(store["products"])):
            
            if(snacker["fave_snack"] == store["products"][i]["title"]):
                snack_list.append(store["products"][i]["title"])
                #print(res1["email"]+ " " + result2["products"][i]["title"] + " "+ result2["products"][i]["variants"][0]["price"])
    print(snack_list)
    snacks = {j:snack_list.count(j) for j in snack_list}

    print(snacks)

def question_two(snackers,store):
    print("******")
    print("Question 2")
    print("******")
    print("Snackers Email Addresses with their favorite snacks")
    for snacker in snackers:
    
        for i in range(len(store["products"])):
            
            if(snacker["fave_snack"] == store["products"][i]["title"]):
                print(snacker["email"]+ ":    " + store["products"][i]["title"])

def question_three(snackers,store):
    print("******")
    print("Question 3")
    print("******")
    total_price = 0
    small_list = []
    price_list= []
    for snacker in snackers:
    
        for i in range(len(store["products"])):
            
            if(snacker["fave_snack"] == store["products"][i]["title"]):
                snack_list.append(store["products"][i]["title"])
                if(store["products"][i]["title"] in small_list):
                    continue
                else:
                    small_list.append(store["products"][i]["title"])
                    price_list.append(float(store["products"][i]["variants"][0]["price"]))
    snacks = {j:snack_list.count(j) for j in snack_list}

    print("*Total Price for each snack*")
    for k in range(len(small_list)):
        item_total = snacks[small_list[k]] * price_list[k]
        print(small_list[k]+": ", item_total)
        total_price += item_total
    print("*Sum Total Price for all snack*")
    print(total_price)
    print("********")
    print("I Love Both of Them!")

if __name__ == '__main__':
    question_one(result1,result2)
    question_two(result1,result2)
    question_three(result1,result2)
