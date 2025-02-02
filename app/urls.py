from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name="index"),
    path('articles/', article_list, name='articles'),
    path("a/<slug:slug>",article_detail, name="article"),  # General slug last
]

