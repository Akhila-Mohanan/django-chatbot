from django.urls import path
from .views import chatbot_api, chatbot_page

urlpatterns = [
    path('', chatbot_page, name='chatbot_page'),  # Webpage for chatbot
    path('api/chat/', chatbot_api, name='chatbot_api'),  # API for chatbot responses
]