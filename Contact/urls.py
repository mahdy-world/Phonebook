from django.urls import path
from .views import *

app_name = 'Contact'
urlpatterns = [
    path('', ContactList.as_view(), name="ContactList"),
    path('create', ContactCreate.as_view(), name="ContactCreate"),
    path('update/<int:pk>', ContactUpdate.as_view(), name="ContactUpdate"),
]