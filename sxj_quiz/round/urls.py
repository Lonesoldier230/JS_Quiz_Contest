from django.urls import path
from .views import Main, common, mix_bag, m_choice, mix_main, recall, g_main

app_name = "round"

urlpatterns = [
    path('',Main.as_view(),name = "main"),
    path('round/<str:round>/<int:iter>', common, name = "common"),
    path('MixedBag/',mix_main, name="mix-main"),
    path('MixedBag/<str:subject>/<int:iter>', mix_bag, name = "mix"),
    path('Multiple/<int:pk>', m_choice, name="multiple"),
    path('Recall/<int:pk>', recall, name="recall"),
    path('general_round/', g_main, name = "general")
]
