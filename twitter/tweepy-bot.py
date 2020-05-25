import tweepy
import time

auth = tweepy.OAuthHandler('yd###DQ####CvvA5h',
                           'NEyVsmz2#########')
auth.set_access_token(
    '125226318#############aL7ynd9###G', 'lDJHAYlRMPgO5B##########fVjHJ##sjJ5Ir')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(500)


search_string = 'shikuroT'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.retweet()
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
