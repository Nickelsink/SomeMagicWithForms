from django.urls import path
from app_test.views import my_first_view, my_second_view

urlpatterns = [
    path('', my_first_view, name="first_view"),
    path('second/', my_second_view, name="second_view")
]
