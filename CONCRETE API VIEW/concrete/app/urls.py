from django.urls import path
from .views import *

urlpatterns = [
    path('teacherapi/',TeacherCreateList.as_view()),
    path('teacherapi/<int:pk>',TeacherUpdateList.as_view()),
]