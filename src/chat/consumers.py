# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import Thread,ChatMessage

class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print("connected",event)

        other_user = self.scope['url_route']['kwargs']['username']
        me = self.scope['user']
        thread_obj = await self.get_thread(me,other_user)        
        # print(other_user,me)
        self.thread_obj = thread_obj
        chat_room = "thread_%s"%thread_obj.id
        self.chat_room = chat_room
        await self.channel_layer.group_add(
        	chat_room,
        	self.channel_name
        )
        await self.send({
        	'type':'websocket.accept'
        	})

    async def websocket_disconnect(self,event):
        print("disconnected",event)

    async def websocket_receive(self,event):
        print("received",event)   
        front_text = event.get('text',None)
        if front_text is not None:
        	loaded_data = json.loads(front_text)
        	msg = loaded_data.get('message')
        	user = self.scope['user']
        	username = 'default'
        	if user.is_authenticated:
        		username = user.username
        	my_response = {
        		"message":msg,
        		"username":username
        	}
        	await self.create_chat_message(msg)
        	# broadcasts the message to be send
        	await self.channel_layer.group_send(
        		self.chat_room,
        		{
        		'type':'chat_message',
        		"text":json.dumps(my_response)
        		}
        	)
        	# print(msg)
        # {'type': 'websocket.receive', 'text': '{"message":"another"}'}
    async def chat_message(self,event):
    	# send the actual message
    	await self.send({
    		'type':'websocket.send',
    		'text':event['text']
    	})

    @database_sync_to_async
    def get_thread(self,user,other_user):
    	return Thread.objects.get_or_new(user,other_user)[0]

    @database_sync_to_async
    def create_chat_message(self,msg):
    	me = self.scope['user']
    	return ChatMessage.objects.create(thread=self.thread_obj,user=me,message=msg)  	