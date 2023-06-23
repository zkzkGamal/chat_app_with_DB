
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Static_Message , chat , new_Static_Message
from datetime import date
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
   
    def disconnect(self , close_code):
        self.channel_layer.group_discard(
            self.room_group_name ,
            self.channel_layer
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json["username"]
        user = text_data_json['user']
        msg_id = text_data_json['msg_id']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username,
                'user':user,
                'msg_id':msg_id
            }
        )
        
    server_msg1 = ''
    usr_ = ''
    id1 = 0
    
    def checkMessage(aa):
        if aa == 0 or aa == '0':
            joob = new_Static_Message.objects.filter(id = (ChatConsumer.id1) )
            return joob
        else:
            joob = new_Static_Message.objects.filter(name = aa , parent = ChatConsumer.id1 )
            return joob
    
    def chat_message(self, event ):
        message = event['message']
        username = event["username"]
        user = event["user"]
        msg_id = event['msg_id']
        
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            "username":username,
            "msg_id":msg_id
        }))
        ChatConsumer.usr_ = username
        # joob = ChatConsumer.checkMessage(message)
        joob = ChatConsumer.checkMessage(message)
        server_massage = ChatConsumer.server_msg1
        if joob:
            if message == 0 or message == '0':
                current_message = new_Static_Message.objects.get(id = ChatConsumer.id1)
                if current_message.parent is not None:
                    aa = new_Static_Message.objects.get(id = current_message.parent.id)
                else:
                    aa = current_message
            else:
                aa = new_Static_Message.objects.get(name=message , parent = ChatConsumer.id1)
            server_massage = aa.message
            ChatConsumer.server_msg1 = server_massage
            ChatConsumer.id1 = aa.id
            self.send(text_data=json.dumps({
                'type':'chat',
                'message':server_massage,
                "username":'server',
                "msg_id":msg_id
            }))
        else:
            self.send(text_data=json.dumps({
                'type':'chat',
                'message':ChatConsumer.server_msg1,
                "username":'server'
            }))
        today = date.today()
        if user == '' or user == "" or user == 'AnonymousUser' : a =1
        else:
            userq = User.objects.get(username = user)
            chat1 = chat(user = userq, message = message , server_message = server_massage, data_sended = today , message_id = (ChatConsumer.id1))
            chat1.save()
            
        
    
    
    



