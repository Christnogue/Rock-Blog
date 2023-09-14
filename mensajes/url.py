from django.urls import path
from mensaje.views import UserListView, MessageDetailView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('usuarios/', UserListView.as_view(), name='user_list'),
    path('mensaje/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('messages/', MessageDetailView.as_view(), name=' messages'),
]
