from django.urls import path
from .views import Main

app_name = "round"

urlpatterns = [
    path('',Main.as_view(),name = "main"),
]
