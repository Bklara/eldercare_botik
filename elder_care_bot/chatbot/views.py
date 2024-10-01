from rest_framework import viewsets  
from chatbot.serializers import DiseaseSerializer, BlogPostSerializer  
from chatbot.models import Disease, BlogPost 

class DiseaseViewSet(viewsets.ModelViewSet):  
    queryset = Disease.objects.all()  
    serializer_class = DiseaseSerializer  

class BlogPostViewSet(viewsets.ModelViewSet):  
    queryset = BlogPost.objects.all()  
    serializer_class = BlogPostSerializer