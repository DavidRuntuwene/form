from nturl2path import url2pathname
from django.urls import URLPattern, path
from unicodedata import name
from . import views

urlpatterns = [
    path("first/", views.func1, name="First1"),
    path("second/", views.func2, name="Second2"),
    path("third/", views.func3, name="Third3"),
    path("forth/", views.func4, name="Fourth4")
]

