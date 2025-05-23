from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # /challenges/

    # Dynamic URL pattern for monthly challenges
    path("<int:month>", views.monthly_challenge_by_number, name="monthly_challenge_by_number"),
    path("<str:month>", views.monthly_challenge, name="monthly-challenge"),
]