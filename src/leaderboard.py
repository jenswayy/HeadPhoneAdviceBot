import praw
import os
import re
import re
from bs4 import BeautifulSoup as BS

sub = "RedditsQuests"

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
password = os.environ.get('pass')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent='r/RedditsQuests bot',
                     username='TheQuestMaster')
                     
for flair in reddit.subreddit('RedditsQuests').flair(limit=None):
    user = flair['user'].name
    flair_css_class = flair['flair_css_class']
    flair_text = flair['flair_text']

f = open(".surge/leaderboard.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open(".surge/leaderboard.txt", "r")
print(f.read())