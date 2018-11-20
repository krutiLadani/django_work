import twitter
import util
from config import *

AHBD_WOEID = 2295402
api = twitter.Api(consumer_key=key, consumer_secret=secret, access_token_key=access_key,
                  access_token_secret=access_secret)


def search(searchTerm):
    """
    Print recent tweets containing `searchTerm`.

    To test this function, at the command line run:
        python twitter_api.py --search=<search term>
    For example,
        python twitter_api.py --search=python
    """
    api = twitter.Api(consumer_key=key, consumer_secret=secret, access_token_key=access_key,
                      access_token_secret=access_secret)
    tweets = api.GetSearch(searchTerm)
    for tweet in tweets:
        print "\n--------------------------------------------------------------------------"
        user = tweet.GetUser()
        print "{0} @{1} {2}\n".format(user.GetName().encode('utf-8').strip(), user.GetScreenName().encode('utf-8').strip()
                                    , user.GetFollowersCount())
        print u'\u204B', tweet.GetText().encode('utf-8').strip()
        print "\nCreated At : ", tweet.GetCreatedAt()
        print "Retweeted : {0} Likes : {1}".format(tweet.GetRetweetCount(), tweet.GetFavoriteCount()).encode(
            'utf-8').strip()


def trendingTopics(location_WOEID):
    """
    Print the currently trending topics.

    To test this function, at the command line run:
        python twitter_api.py -t
    """
    api = twitter.Api(consumer_key=key, consumer_secret=secret, access_token_key=access_key,
                      access_token_secret=access_secret)
    trending_topics = api.GetTrendsWoeid(location_WOEID)
    i = 1
    for topic in trending_topics:
        if i == 11:
            break
        else:
            print "Topic #{0}".format(i)
            i += 1
            util.safe_print(topic.name)


def userTweets(username):
    """
    Print recent tweets by `username`.

    You may find the twitter.Api() function GetUserTimeline() helpful.

    To test this function, at the command line run:
        python twitter_api.py -u <username>
    For example,
        python twitter_api.py -u bostonpython
    """
    api = twitter.Api(consumer_key=key, consumer_secret=secret, access_token_key=access_key,
                      access_token_secret=access_secret)
    tweets = api.GetUserTimeline(screen_name=username)
    i = 1
    for tweet in tweets:
        print "\n--------------------------------------------------------------------------"
        user = tweet.GetUser()
        print "{0} @{1} {2}\n".format(user.GetName().encode('utf-8').strip(), user.GetScreenName().encode('utf-8').strip()
                                    , user.GetFollowersCount())
        print u'\u204B', tweet.GetText().encode('utf-8').strip()
        print "\nCreated At : ", tweet.GetCreatedAt()
        print "Retweeted : {0} Likes : {1}".format(tweet.GetRetweetCount(), tweet.GetFavoriteCount()).encode(
            'utf-8').strip()


def trendingTweets():
    """
    Print tweets for all the trending topics.

    To test this function, at the command line run:
        python twitter_api.py -w
    """
    api = twitter.Api(consumer_key=key, consumer_secret=secret, access_token_key=access_key,
                      access_token_secret=access_secret)
    trending_topics = api.GetTrendsWoeid(AHBD_WOEID)
    topic_no = 1
    for topic in trending_topics:
        if topic_no == 11:
            break
        else:
            print "\n***************** Tweets on the Topic {0} **********************".format(topic.name.encode('utf-8').strip())
            topic_no += 1

            tweets = api.GetSearch(topic.name)
            tweet_no = 1
            for tweet in tweets:
                if tweet_no == 3:
                    break
                else:
                    user = tweet.GetUser()
                    print "\n-----------------------------------"
                    print "{0} @{1} {2}\n".format(user.GetName().encode('utf-8').strip(),
                                                  user.GetScreenName().encode('utf-8').strip()
                                                  , user.GetFollowersCount())
                    print u'\u204B', tweet.GetText().encode('utf-8').strip()
                    print "\nCreated At : ", tweet.GetCreatedAt()
                    print "Retweeted : {0} Likes : {1}".format(tweet.GetRetweetCount(),
                                                               tweet.GetFavoriteCount()).encode(
                        'utf-8').strip()
                    tweet_no += 1
