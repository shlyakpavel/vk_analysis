from download import *
from analyze import *
from porter import Porter

#all_history = get_history(friends, SLEEP_TIME)
for message in all_history:
    if type(message) == dict:
        print(message['body'])
save_to_file(all_history, 'raw.txt')
self_messages = get_messages_for_user(all_history, SELF_ID)
save_to_file(self_messages, 'sm_corpus.txt')
classifier=trainAnger()
print(classifier.classify(format_sentence("Кусь")))