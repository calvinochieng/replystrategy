from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name="index"),
    path("<slug:slug>/",detail_view, name="detail"),  # General slug last
]

