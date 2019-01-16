import requests
from bs4 import BeautifulSoup
import re, csv, json, time, types

def get_facebook(url):
        if ("facebook.com" in url) or ("fb.com" in url):
            res = re.sub(r"#.?/","",url)
            return res

def get_twitter(url):
    if ("twitter.com" in url) or ("twttr.com" in url):
        res = re.sub(r"#.?/","",url)
        return res

def get_linkedin(url):
    if "linkedin.com" in url:
        res = re.sub(r"#.?/","",url)
        return res

def get_youtube(url):
    if "youtube.com" in url:
        res = re.sub(r"#.?/","",url)
        return res

def get_instagram(url):
    if "instagram.com" in url:
        res = re.sub(r"#.?/","",url)
        return res

def get_googleplus(url):
    if "plus.google.com" in url:
        res = re.sub(r"#.?/","",url)
        return res

def facebook_url(fb_list):
    if len(fb_list) == 0:
        return "";
    elif len(fb_list) == 1:
        fb_url = "".join(fb_list)
        return fb_url
    else:
        fb_url = fb_list[0]
        return fb_url

def twitter_url(tw_list):
    if len(tw_list) == 0:
        return "";
    elif len(tw_list) == 1:
        tw_url = "".join(tw_list)
        return tw_url
    else:
        tw_url = tw_list[0]
        return tw_url

def linkedin_url(ln_list):
    if len(ln_list) == 0:
        return "";
    elif len(ln_list) == 1:
        ln_url = "".join(ln_list)
        return ln_url
    else:
        ln_url = ln_list[0]
        return ln_url

def youtube_url(yb_list):
    if len(yb_list) == 0:
        return "";
    elif len(yb_list) == 1:
        yb_url = "".join(yb_list)
        return yb_url
    else:
        yb_url = yb_list[0]
        return yb_url

def instagram_url(ig_list):
    if len(ig_list) == 0:
        return "";
    elif len(ig_list) == 1:
        ig_url = "".join(ig_list)
        return ig_url
    else:
        ig_url = ig_list[0]
        return ig_url

def googleplus_url(gl_list):
    if len(gl_list) == 0:
        return "";
    elif len(gl_list) == 1:
        gl_url = "".join(gl_list)
        return gl_url
    else:
        gl_url = gl_list[0]
        return gl_url

def save_info(s_list = []):
        with open("social_media.json","w+") as jsonFile:
                json.dump(s_list,jsonFile,indent=4)
        with open("social_media.csv","w+") as filer:
                csvwriter = csv.writer(filer)

                count = 0
                for s_row in s_list:
                        if count == 0:
                                csv_head = s_row.keys()
                                csvwriter.writerow(csv_head)

                                count += 1
                        newList = []
                        for social in s_row.values():
                                if type(social) is types.UnicodeType:
                                        newList.append(social.encode("utf-8"))
                                else:
                                        newList.append(social)
                        csvwriter.writerow(newList)

with open("Handle_test.csv", "r+") as csvfile:
    files = csv.reader(csvfile, delimiter=" ")
    i = 0
    social_list = []
    
    for row in files:
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        result = "".join(row)
        timeout = 10
        try:
                init_response = requests.get(result, timeout=timeout)
                init_req = init_response
                init_response.close()
                try:
                        response = requests.get(init_req.url, headers=header, timeout=timeout)
                        req = response
                        response.close()
                except requests.exceptions.NewConnectionError as e:
                        print "Re-Establishing Connection, wait for 15 seconds"
                        time.sleep(15)
                        try:
                                response = requests.get(init_req.url, headers=header, timeout=timeout)
                                req = response
                                response.close()
                        except requests.exceptions.NewConnectionError as e:
                                print "Unable to Connect"
                                pass
                        except requests.exceptions.RequestException as e:
                                print "Unable to Connect"
                                pass
                except requests.exceptions.ConnectTimeoutError as e:
                        print "Re-Establishing Connection, wait for 10 seconds"
                        time.sleep(10)
                        try:
                                response = requests.get(init_req.url, headers=header, timeout=30)
                                req = response
                                response.close()
                        except requests.exceptions.ConnectTimeoutError as e:
                                print "Unable to Connect"
                                pass
                        except requests.exceptions.RequestException as e:
                                print "Unable to Connect"
                                pass
                except requests.exceptions.RequestException as e:
                        print e
                        pass

        except requests.exceptions.NewConnectionError as e:
                print "Re-Establishing Connection, wait for 15 seconds"
                time.sleep(15)
                try:
                        init_response = requests.get(result, timeout=timeout)
                        init_req = init_response
                        init_response.close()
                        try:
                                response = requests.get(init_req.url, headers=header, timeout=timeout)
                                req = response
                                response.close()
                        except requests.exceptions.NewConnectionError as e:
                                print "Re-Establishing Connection, wait for 15 seconds"
                                time.sleep(15)
                                try:
                                        response = requests.get(init_req.url, headers=header, timeout=timeout)
                                        req = response
                                        response.close()
                                except requests.exceptions.NewConnectionError as e:
                                        print "Unable to Connect"
                                        pass
                                except requests.exceptions.RequestException as e:
                                        print "Unable to Connect"
                                        pass
                        except requests.exceptions.ConnectTimeoutError as e:
                                print "Re-Establishing Connection, wait for 10 seconds"
                                time.sleep(10)
                                try:
                                        response = requests.get(init_req.url, headers=header, timeout=30)
                                        req = response
                                        response.close()
                                except requests.exceptions.ConnectTimeoutError as e:
                                        print "Unable to Connect"
                                        pass
                                except requests.exceptions.RequestException as e:
                                        print "Unable to Connect"
                                        pass
        
        except requests.exceptions.ConnectTimeoutError as e:
                print "Re-Establishing Connection, wait for 10 seconds"
                time.sleep(10)
                try:
                        init_response = requests.get(result, timeout=timeout)
                        init_req = init_response
                        init_response.close()
                        try:
                                response = requests.get(init_req.url, headers=header, timeout=30)
                                req = response
                                response.close()
                        except requests.exceptions.NewConnectionError as e:
                                print "Re-Establishing Connection, wait for 15 seconds"
                                time.sleep(15)
                                try:
                                        response = requests.get(init_req.url, headers=header, timeout=timeout)
                                        req = response
                                        response.close()
                                except requests.exceptions.NewConnectionError as e:
                                        print "Unable to Connect"
                                        pass
                                except requests.exceptions.RequestException as e:
                                        print "Unable to Connect"
                                        pass
                        except requests.exceptions.ConnectTimeoutError as e:
                                print "Re-Establishing Connection, wait for 10 seconds"
                                time.sleep(10)
                                try:
                                        response = requests.get(init_req.url, headers=header, timeout=30)
                                        req = response
                                        response.close()
                                except requests.exceptions.ConnectTimeoutError as e:
                                        print "Unable to Connect"
                                        pass
                                except requests.exceptions.RequestException as e:
                                        print "Unable to Connect"
                                        pass
                
        except requests.exceptions.RequestException as e:
                print e
                pass
        
        fb_list = []
        tw_list = []
        ig_list = []
        gl_list = []
        yb_list = []
        ln_list = []
        
        soup = BeautifulSoup(req.content,"html.parser")
        for link in soup.find_all('a',href=True):
            url = link["href"].encode("utf-8")
            fb_list.append(get_facebook(url))
            tw_list.append(get_twitter(url))
            ig_list.append(get_instagram(url))
            yb_list.append(get_youtube(url))
            gl_list.append(get_googleplus(url))
            ln_list.append(get_linkedin(url))
        i += 1
        fb_list = list(filter(None,fb_list))
        tw_list = list(filter(None,tw_list))
        ig_list = list(filter(None,ig_list))
        yb_list = list(filter(None,yb_list))
        gl_list = list(filter(None,gl_list))
        ln_list = list(filter(None,ln_list))
        if type(soup.find('title')) is types.NoneType:
                title = ""
        else:
                title = soup.find('title').get_text()

        social_list.append( {"Name": title.encode("utf-8"),
                       "Website": req.url.encode("utf-8"),
                       "Facebook_Url" : facebook_url(fb_list),
                       "Twitter_Url" : twitter_url(tw_list),
                       "Instagram_Url" : instagram_url(ig_list),
                       "Youtube_Url" : youtube_url(yb_list),
                       "GooglePlus_Url" : googleplus_url(gl_list),
                       "Linkedin_Url" : linkedin_url(ln_list)})
        save_info(social_list)
        print i, "th"
        print "Sleep for 15 seconds"
        time.sleep(15)
