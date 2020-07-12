import praw
import os
import re
import json

sub = "BobbbayBots"

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
password = os.environ.get('pass') 

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent='r/HeadphoneAdvice bot',
                     username='MasterOfHeadphones')

moderators = list(reddit.subreddit(sub).moderator())
for submission in reddit.subreddit(sub).new(limit=None):
    print(submission.title)
    submission.comments.replace_more(limit=None)
    if submission.saved is False:
        print("Submission is not saved yet xD")
        for comment in submission.comments.list():
            print("Going through comments")
            if ((("!thanks" in comment.body)) and ((comment.is_submitter) or (comment.author in moderators)) and (comment.parent().author.name is not submission.author.name)):
                if comment.parent().author_flair_text and comment.parent().author_flair_text.endswith("Ω"):
                    count_taker = int(comment.parent().author_flair_text.replace("Ω","")) 
                    count_taker += 1 
                    taker_flair = "{0}Ω".format(count_taker)
                    reddit.subreddit(sub).flair.set(comment.parent().author.name, taker_flair, "thanked")
                else:
                    reddit.subreddit(sub).flair.set(comment.parent().author.name, "1Ω", "thanked")
                submission.save()
                reply = 'This advice thread has been answered! [Here](https://reddit.com/r/{0}/comments/{1}/{2}/{3}/) is the link to the answer. \n\n^Beep ^boop^.'.format(sub, submission.id, submission.title, comment.parent().id)
                submission.reply(reply).mod.distinguish(sticky=True)
                print("Finished!")
    else:
        continue