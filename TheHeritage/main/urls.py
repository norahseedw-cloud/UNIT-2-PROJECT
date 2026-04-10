from django.urls import path
from . import views
app_name = "main"


urlpatterns = [
    path('',views.home_view, name="home_view"),
    path('traditional-clothing/',views.clothing_view, name="clothing_view"),
    path('traditional-foods/',views.foods_view, name="foods_view"),
]
