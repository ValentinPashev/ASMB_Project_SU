from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts import views
from accounts.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update/', views.create_profile_or_display_view, name='update_profile'),

]