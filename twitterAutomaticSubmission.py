import tweepy
import random
from datetime import datetime, timedelta
import time

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate and create an API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Winnie the Pooh quotes
quotes = [
    "The things that make me different are the things that make me."	,
    "A little consideration, a little thought for others, makes all the difference."	,
    "You can't stay in your corner of the Forest waiting for others to come to you. You have to go to them sometimes."	,
    "I'm not lost, for I know where I am. But however, where I am may be lost."	,
    "Some people care too much. I think it's called love."	,
    "Rivers know this: there is no hurry. We shall get there some day."	,
    "How lucky I am to have something that makes saying goodbye so hard."	,
    "Don't underestimate the value of Doing Nothing, of just going along, listening to all the things you can't hear, and not bothering."	,
    "Promise me you'll always remember: You're braver than you believe and stronger than you seem, and smarter than you think."	,
    "I don't live in either my past or my future. I'm interested only in the present. If you can concentrate always on the present, you'll be a happy man."	,
    "If the person you are talking to doesn't appear to be listening, be patient. It may simply be that he has a small piece of fluff in his ear."	,
    "Think, think, think."	,
    "It's not much of a tail, but I'm sort of attached to it."	,
    "A day without a friend is like a pot without a single drop of honey left inside."	,
    "You're braver than you believe, and stronger than you seem, and smarter than you think."	,
    "I am a bear of very little brain, and long words bother me."	,
    "Sometimes the smallest things take up the most room in your heart."	,
    "The more that you read, the more things you will know. The more that you learn, the more places you'll go."	,
    "Whenever you find yourself doubting how far you can go, just remember how far you have come."	,
    "The best things in life are the people we love, the places we've been, and the memories we've made along the way."	,
    "A little kindness goes a long way."	,
    "Weeds are flowers too, once you get to know them."	,
    "Life is a journey to be experienced, not a problem to be solved."	,
    "I used to believe in forever, but forever was too good to be true."	,
    "Love is taking a few steps backward, maybe even more... to give way to the happiness of the person you love."	,
]

# Get the current time
now = datetime.now()

# Schedule the tweet for 8am the next day
target_time = datetime(now.year, now.month, now.day, 8) + timedelta(days=1)

# Sleep until 8am the next day
time.sleep((target_time - now).seconds)

# Post a tweet with a random quote
api.update_status(random.choice(quotes))
