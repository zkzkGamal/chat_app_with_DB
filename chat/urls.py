from django.urls import path 
from . import views 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.lobby),
    path('base', views.base),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    path('webhook',views.webhook_view,name='webhook'),
    path("rest",views.getdata),
    path("rest1",views.getData1),
    # path("rest1post",views.postData),
    
]