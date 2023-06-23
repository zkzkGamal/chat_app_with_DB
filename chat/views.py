from django.shortcuts import render
from .models import chat ,Static_Message , new_Static_Message
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer , ItemSerializer1 , ItemSerializer2
from .consumers import ChatConsumer
import random
# Create your views here.

def randGreating():
    greating =new_Static_Message.objects.get(level = 0)
    # random1 = random.randint(0,(len(greating)-1))
    # return greating[random1].message
    return greating

def randGreatingName(company_name):
    greating =Static_Message.objects.filter(perant_id = 0 ,company_name = company_name)
    random1 = random.randint(0,(len(greating)-1))
    return greating[random1].message

def lobby(request):
    chat1 = ''
    user = request.user.is_authenticated
    if user:
        user = request.user
        chat1 = chat.objects.filter(user = user) 
        if chat1:
            ChatConsumer.server_msg1 = chat1.last().server_message
            ChatConsumer.id1 = chat1.last().message_id
        else:
            ChatConsumer.server_msg1 = randGreating().message
            ChatConsumer.id1 = randGreating().id
    else:
            ChatConsumer.server_msg1 = randGreating().message
            ChatConsumer.id1 = randGreating().id        
    return render(request, 'chat/lobby.html' , {'chat':chat1  })

def base(request):
    return render(request,'chat/base.html')

@api_view(['GET'])
def getdata(request):
    msgs = Static_Message.objects.all()
    serializer = ItemSerializer(msgs , many =True)
    return Response(serializer.data)

@api_view(['GET'])
def getData1(request):
    msgs = new_Static_Message.objects.all()
    serializer = ItemSerializer2(msgs , many =True)
    return Response(serializer.data)

# @api_view(['POST'])
# def postData(request):
#     serializer = ItemSerializer1(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook_view(request):
    if request.method == 'POST':
        # Process the data received from the PHP site
        data = request.POST.get('data')  # Access the data sent in the POST request
        # Perform any required actions or processing with the data
        return render(request,'chat/index.html',{"aa":data})
        # return HttpResponse('Webhook received successfully', status=200)
    else:
        # return HttpResponse('Method not allowed', status=405)
        return render(request, 'chat/index.html',{'aa':data})
    

