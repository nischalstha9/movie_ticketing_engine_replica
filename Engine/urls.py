from django.urls import path
from .views import seatview
urlpatterns = [
    path("", seatview, name="home")
]