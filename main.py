from pyrogram import Client
from telethon import TelegramClient, events
import asyncio
import requests


api_id = 7628507
api_hash = "8511ba76e082e7f0cc3f69e59c730036"

my_channel_id = "me"
channels = [-1001598203309]

#  d69a10ae5fd68b5c6879640a924aa4d39334d115d84e5281e25af21e19f0d54f4d9bba259086803e56b41

client = TelegramClient('myGrab', api_id, api_hash)
print("FINISH HIM!")

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    if event.message:
        token = 'd69a10ae5fd68b5c6879640a924aa4d39334d115d84e5281e25af21e19f0d54f4d9bba259086803e56b41'
        group_id = 205926916
        owner_id_group = -205926916
        foo = event.message
        #  main = requests.post('https://api.vk.com/method/photos.getWallUploadServer?',data={
            #  'group_id': group_id,
            #  'access_token': token,
            #  'v': '5.130',
        #  }).json()['response']
        #  response = main['upload_url']

        #  answer = requests.post(response, data={'photo': 'error.jpg'}).json()

        requests.post('https://api.vk.com/method/wall.post?', data={
            'access_token': token,
            'owner_id': owner_id_group,
            'message': foo.message,
            'v':"5.130",
            'scope':'wall',
            'from_group':1
        })
 
client.start()
client.run_until_disconnected()

