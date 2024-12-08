from django.urls import path

from campaigns import views

urlpatterns = [
    path('report/', views.pass_campaign_report, name='report'),
]