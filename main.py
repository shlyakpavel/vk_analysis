#!/usr/bin/env python3

from download import *
from analyze import trainLove
from analyze import format_sentence
from porter import Porter
from operator import itemgetter, attrgetter
from os import system
import time

#Download messages
SLEEP_TIME = 0.3
all_history = get_history(friends, SLEEP_TIME)
#Prepare train data
system("./build_data.sh")
#Train
classifier=trainLove()
#Count everything
realations = []
for friend in friends:
    neg =0
    pos =0
    for message in all_history:
        if type(message) == dict:
            #print(message['target'] - friend)
            if ( message['target'] == friend) and (message['uid'] == SELF_ID) :
                if classifier.classify(format_sentence(message['body'].lower())) == "neg":
                    neg = neg + 1
                else:
                    #print(message['body'])
                    pos = pos + 1
    #Output
    if (pos != 0):
        realation = {}
        profiles = vkapi.users.get(user_id=friend)
        full_name=profiles[0]['first_name']+' '+profiles[0]['last_name']
        time.sleep(SLEEP_TIME)
        realation['name']=full_name
        realation['status']=pos/(neg+pos)
        realations.append(realation)
        #print("With " + full_name + " you are romantic by " + str(pos/(neg+pos)) + " percent")
print(sorted(realations, key=itemgetter('status'), reverse=True))
#save_to_file(all_history, 'raw.txt')
self_messages = get_messages_for_user(all_history, SELF_ID)
#save_to_file(self_messages, 'sm_corpus.txt')