from django.urls import path
from . import views
from hello_azure import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('description/', views.getDescription),

]