from rest_framework import serializers  
from .models import Disease, BlogPost  

class DiseaseSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Disease  
        fields = '__all__'  

class BlogPostSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = BlogPost  
        fields = '__all__'


