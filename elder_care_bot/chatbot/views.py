from rest_framework import viewsets  
from rest_framework.decorators import api_view  
from rest_framework.response import Response  
from chatbot.models import Disease, BlogPost  
from chatbot.serializers import DiseaseSerializer, BlogPostSerializer  
from chatbot.chatbot_logic import process_user_input  

class DiseaseViewSet(viewsets.ModelViewSet):  
    queryset = Disease.objects.all()  
    serializer_class = DiseaseSerializer  

class BlogPostViewSet(viewsets.ModelViewSet):  
    queryset = BlogPost.objects.all()  
    serializer_class = BlogPostSerializer  

@api_view(['POST'])  
def chat_view(request):  
    user_input = request.data.get('message', '')  
    response = process_user_input(user_input)  
    return Response({'response': response})


from django.shortcuts import render  

def chat_page(request):  
    return render(request, 'chatbot/index.html')