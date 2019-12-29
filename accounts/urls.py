from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import LoginView, RegisterView, ProfileView,delete_user

app_name = 'accounts'

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('delete/', delete_user, name='delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
