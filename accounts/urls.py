# myproject/urls.py

from django.contrib import admin
from django.urls import path
from accounts.views import GetUserView, RegisterView, LoginView,UpdateUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('get-user/', GetUserView.as_view(), name='get-user'),
    path('update-user/', UpdateUserView.as_view(), name='get-user'),
]
