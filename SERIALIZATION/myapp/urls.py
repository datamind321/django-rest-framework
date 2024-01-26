from django.urls import path
from .views import student_view,teacher_view
urlpatterns = [
    path('student/',student_view,name='student-data'),
    path('teacher/',teacher_view,name='teacher-data'),
]