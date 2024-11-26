from django.urls import path

from students import views

urlpatterns = [
    path('student/', views.student_info, name='student_info'),
]