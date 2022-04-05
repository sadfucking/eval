import vk_api, traceback, time
from datetime import datetime
import os, math, subprocess
from vk_api.longpoll import VkEventType, VkLongPoll
import math, subprocess, re, random
token='' # токен

_vk_=vk_api.VkApi(token=token)
vk=_vk_.get_api()
longpoll=VkLongPoll(_vk_)
def reply_txt(msg_id):
        text=vk.messages.getById(message_ids=msg_id)['items'][0]['reply_message']['text']
        return text

while True:
	try:
		for event in longpoll.listen():
			if event.type == VkEventType.MESSAGE_NEW and event.from_me:
				time_=event.raw[4]
				cmd=event.text.lower()
				peer_id=event.peer_id
				message_id=event.message_id

				if cmd[0]=='к':
				    t=cmd[2:]
				    proc=subprocess.Popen([str(t)], stdout=subprocess.PIPE)
				    out=proc.stdout.read().decode('utf-8')
				    vk.messages.edit(peer_id=peer_id, message=out, message_id=message_id)
				if cmd[0]=='т':
					r=eval(cmd[1:])
					vk.messages.edit(peer_id=peer_id, message=r, message_id=message_id)
	except:
		print('Я падаю.')
		traceback.print_exc()
		time.sleep(5)
