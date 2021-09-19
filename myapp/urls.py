from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('',home,name = "home"),
    path('view', view, name="view"),
    path('transactions',tran, name = "tran"),
    path('transfer',transfer,name="transfer")
]
