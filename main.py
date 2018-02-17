from download import *
from analyze import trainAnger
from analyze import format_sentence
from porter import Porter
from os import system

#Download messages
SLEEP_TIME = 0.3
#all_history = get_history(friends, SLEEP_TIME)
#Prepare train data
os.system("./build_data.sh")
#Train
classifier=trainAnger()
#Count everything
neg =0
pos =0
for message in all_history:
    if type(message) == dict:
        if classifier.classify(format_sentence(message['body'])) == "neg":
            neg = neg + 1
        else:
            print(message['body'])
            pos = pos + 1
#Output
print("You are romantic by " + str(pos/(neg+pos)) + " percent")
save_to_file(all_history, 'raw.txt')
self_messages = get_messages_for_user(all_history, SELF_ID)
save_to_file(self_messages, 'sm_corpus.txt')