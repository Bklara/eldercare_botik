from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from chatbot.views import DiseaseViewSet, BlogPostViewSet  

router = DefaultRouter()  
router.register(r'diseases', DiseaseViewSet)  
router.register(r'blog', BlogPostViewSet)  

urlpatterns = [  
    path('api/', include(router.urls)),  
]