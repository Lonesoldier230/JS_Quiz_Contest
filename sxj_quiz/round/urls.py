from django.urls import path
from .views import Main, common, mix_bag, visual_a, m_choice, mix_main

app_name = "round"

urlpatterns = [
    path('',Main.as_view(),name = "main"),
    path('round/<str:round>/<int:iter>', common, name = "common"),
    path('MixedBag/',mix_main, name="mix-main"),
    path('MixedBag/<str:subject>/<int:iter>', mix_bag, name = "mix"),
    path('AudioVisual/<int:pk>', visual_a, name="auvis"),
    path('Multiple/<int:pk>', m_choice, name="multiple")
]
