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
                     username='TheQuestMaster')

flairsInSub = ""
for flair in reddit.subreddit(sub).flair(limit=None):
    flairsInSub += "{}".format(flair)
f = open("../TheQuestMasterLeaderboard/main.txt", "w")
f.write(flairsInSub)
f.close()

def find(string): 
    match = re.search(r"(?:[\w]+)?://[^/\s?#]+[^\s?#]+(?:\?[^\s#]*)?(?:#[^\s]*)?", string)
    if(match):
      return True;
    else:
      return False;

moderators = list(reddit.subreddit(sub).moderator())
for submission in reddit.subreddit(sub).new(limit=None):
    print("Started")
    print(submission.title)
    submission.comments.replace_more(limit=None)
    print("Replaced more?")
    if submission.saved is False:
        print("Submission is not saved yet xD")
        for comment in submission.comments.list():
            print("Going through comments")
            if ((("!completed" in comment.body)) and ((comment.is_submitter) or (comment.author in moderators)) and (comment.parent().author.name is not submission.author.name)):
                if(find(comment.parent().body)):
                    #if(find(comment.parent().body) != []):
                    print("Wow big if statement")
                    count_op_str = submission.author_flair_text
                    try:
                        print("Trying this thing I should not be doing xD")
                        if ( count_op_str is not None or count_op_str != ""):
                            count_op = int(count_op_str.replace("ᚬ", ""))
                            count_op += 1
                            op_flair = "{0}ᚬ".format(count_op)
                            reddit.subreddit(sub).flair.set(submission.author.name, op_flair, "QuestFairer")
                        else:
                            reddit.subreddit(sub).flair.set(submission.author.name, "1ᚬ", "QuestFairer")
                    except:
                        print("You have been accepted")
                    if comment.parent().author_flair_text and comment.parent().author_flair_text.endswith("ᚬ"):
                        print("Adding to the old quest doer")
                        count_taker = int(comment.parent().author_flair_text.replace("ᚬ",""))
                        count_taker += 2
                        taker_flair = "{0}ᚬ".format(count_taker)
                        reddit.subreddit(sub).flair.set(comment.parent().author.name, taker_flair, "QuestFairer")
                    else:
                        print("Adding to the new quest doer")
                        reddit.subreddit(sub).flair.set(comment.parent().author.name, "2ᚬ", "QuestFairer")
                    print("All done, adding flairs now")
                    print(submission.flair.choices())
                    submission.flair.select(None, "Completed!")
                    submission.save()
                    reply = 'This quest has been completed, but feel free to go ahead and recomplete this quest! \n\n^Beep ^boop^.'
                    submission.reply(reply).mod.distinguish(sticky=True)
                    print("Finished! Breaking...")
                else:
                    print("No link buddy!")
                    comment.mod.remove()
                    submission.author.message('Your comment in r/redditsquests has been removed', 'We only allow approvals that contain links. It\'s not your fault, but next time make sure the person who has completed the quest provides a link. PM u/MaxwellIsSmall for questions about this sub\'s rules and u/Bobbbay for any questions, concerns, or comments about the bot. ')
        else:
            continue
