from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('send-email/<str:email_address>/', send_email),
    path('admin/', admin.site.urls),
]
