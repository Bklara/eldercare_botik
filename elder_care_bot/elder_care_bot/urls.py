from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from chatbot.views import DiseaseViewSet, BlogPostViewSet, chat_view, chat_page  

router = DefaultRouter()  
router.register(r'diseases', DiseaseViewSet)  
router.register(r'blog', BlogPostViewSet)  

urlpatterns = [  
    path('', chat_page, name='chat_page'),  
    path('api/', include(router.urls)),  
    path('api/chat/', chat_view, name='chat'),  
]