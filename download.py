#!/usr/bin/env python3
import vk
import time
import re
import os

from porter import Porter

#Auth
os.system('./main.sh')
f=open('token.key')
lines=f.readlines()

APP_ID=6375523
access_token = lines[1].strip()
session = vk.Session(access_token=access_token)
vkapi = vk.API(session)

SELF_ID = int(lines[2].strip())
TARGET_ID = 249694608
SLEEP_TIME = 0.3

friends = vkapi('friends.get') # получение всего списка друзей для текущего пользователя

def get_dialogs(user_id):
	dialogs = vkapi('messages.getDialogs', user_id=user_id)
	return dialogs

def get_history(friends, sleep_time=0.3):
	all_history = []
	i = 0
	for friend in friends:
		friend_dialog = get_dialogs(friend)
		time.sleep(sleep_time)
		dialog_len = friend_dialog[0]
		friend_history = []
		if dialog_len > 200:
			resid = dialog_len
			offset = 0
			while resid > 0:
				friend_history += vkapi('messages.getHistory', 
					user_id=friend, 
					count=200, 
					offset=offset)
				time.sleep(sleep_time)
				resid -= 200
				offset += 200
				if resid > 0:
					print('--processing', friend, ':', resid, 
						'of', dialog_len, 'messages left')
			all_history += friend_history
		i +=1
		print('processed', i, 'friends of', len(friends))
	return all_history

def get_messages_for_user(data, user_id):
	self_messages = []
	for dialog in data:
		if type(dialog) == dict:
			if dialog['uid'] == user_id and dialog['from_id'] == user_id:
				m_text = re.sub("<br>", " ", dialog['body'])
				self_messages.append(m_text)
	print('Extracted', len(self_messages), 'messages in total')
	return self_messages

def save_to_file(data, file_name='output.txt'):
	with open(file_name, 'w', encoding='utf-8') as f:
	    print(data, file=f)

if __name__ == '__main__':
    all_history = get_history(friends, SLEEP_TIME)
    for message in all_history:
        try:
            print(Porter.stemstr(message['body']))
        except:
            print('This is an error message!')
    save_to_file(all_history, 'raw.txt')
    self_messages = get_messages_for_user(all_history, SELF_ID)
    save_to_file(self_messages, 'sm_corpus.txt')