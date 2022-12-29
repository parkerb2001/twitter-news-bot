import tweepy
import requests
import json
import time

#All keys and tokens needed in order to access twitter API
consumerKey = ""
consumerSecret = ""
accessToken = ""
accessTokenSecret = ""

#Calls authentication handler objects and then instantiates api with handler.
auth = tweepy.OAuth1UserHandler(consumerKey, consumerSecret, accessToken, accessTokenSecret)
api = tweepy.API(auth)

#Sends tweet with API based on text passed in
def tweet(content):
    hashtags = "#Crypto $BTC #Ethereum"
    api.update_status(content + " \n" + hashtags)

#Retrieves the URL articles from the newsdata.io API and returns the most recent article title and link
def getNews(url):
    raw = requests.get(url)
    loadedDict = json.loads(raw.text)
    articles = loadedDict["results"]
    title = articles[0]["title"]
    url = articles[0]["link"]
    return {"title" : title, "url" : url}

#Tweets article title and link every two hours.
def main():
    while True:
        newsAPI = ""
        article = getNews(newsAPI)
        title = article["title"]
        link = article["url"]

        try:
            tweet(title + " \n" + link)
            print("Tweeting!")
            lastTitle = title
        except Exception as e:
            print(e)
        time.sleep(14400)


main()
