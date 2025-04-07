from .views import CustomLoginView, user_register
from django.urls import path



urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', user_register, name='register'),
    #path('logout/', views.user_logout, name='logout'),
]