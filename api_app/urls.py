from django.urls import path
from . import views

urlpatterns =[
    path('student_create/',views.student_create, name = 'student_create'),
]