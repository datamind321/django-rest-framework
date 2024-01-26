from django.urls import path 
from .views import *

urlpatterns = [
    path('studentapi/',StudentListView.as_view()),
    path('studentapi/<int:pk>',StudentView.as_view()),

]