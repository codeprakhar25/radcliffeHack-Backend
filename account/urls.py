from django.urls import path
from .views import GetUserFromToken, GetUserView, RegisterUserView, LoginView, UpdateUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', GetUserView.as_view(), name='get_user'),
    path('user/update/', UpdateUserView.as_view(), name='update_user'),
     path('get-user/', GetUserFromToken.as_view(), name='get_user_from_token'),
]