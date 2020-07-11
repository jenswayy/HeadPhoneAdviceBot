import praw
import os
import re

sub = "RedditsQuests"

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
password = os.environ.get('pass')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent='r/RedditsQuests bot',
                     username='TheQuestMaster')

submissions = reddit.subreddit(sub).new(limit=None)
print(submissions)

#for submission in submissions:
#  if (submission.saved is False):
#    for comment in submission.comments.list():
#      if ((("!completed" in comment.body)) and ((comment.is_submitter) or ('RedditsQuests' in comment.author.moderated())) and (comment.parent().author.name is not submission.author.name)):

gen = (submission for submission in submissions if submission.saved is False)

for x in gen:
    x.comments.replace_more()
    ggen = (comment for comment in x.comments.list() if ("!completed" in comment.body) if (comment.is_submitter) if (comment.parent().author.name is not x.author.name))
    for xx in ggen: 
      print(xx.body)