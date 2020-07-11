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
                     user_agent='r/RedditsQuests bot',
                     username='TheQuestMaster') #! fix this

moderators = list(reddit.subreddit(sub).moderator())
for submission in reddit.subreddit(sub).new(limit=None):
    print(submission.title)
    submission.comments.replace_more(limit=None)
    if submission.saved is False:
        print("Submission is not saved yet xD")
        for comment in submission.comments.list():
            print("Going through comments")
            if ((("!thanks" in comment.body)) and ((comment.is_submitter) or (comment.author in moderators)) and (comment.parent().author.name is not submission.author.name)):
                '''count_op_str = submission.author_flair_text
                try:
                    print("Trying this thing I should not be doing xD")
                    if ( count_op_str is not None or count_op_str != ""):
                        count_op = int(count_op_str.replace("ᚬ", ""))
                        count_op += 1
                        op_flair = "{0}ᚬ".format(count_op)
                        reddit.subreddit(sub).flair.set(submission.author.name, op_flair, "thanked")
                    else:
                        reddit.subreddit(sub).flair.set(submission.author.name, "1ᚬ", "thanked")
                except:
                    print("You have been accepted")'''
                if comment.parent().author_flair_text and comment.parent().author_flair_text.endswith("ᚬ"): #! Edit currency
                    count_taker = int(comment.parent().author_flair_text.replace("ᚬ","")) #! Here too
                    count_taker += 1 
                    taker_flair = "{0}ᚬ".format(count_taker) #! Here as well
                    reddit.subreddit(sub).flair.set(comment.parent().author.name, taker_flair, "thanked")
                else:
                    reddit.subreddit(sub).flair.set(comment.parent().author.name, "1ᚬ", "thanked") #! Lastly, here
                #submission.flair.select(None, "Answered!")
                submission.save()
                reply = 'This advice thread has been answered! [Here](https://reddit.com/r/{0}/comments/{1}/{2}/{3}/) is the link to the answer. \n\n^Beep ^boop^.'.format(sub, submission.id, submission.title, comment.id)
                submission.reply(reply).mod.distinguish(sticky=True)
                print("Finished!")
    else:
        continue