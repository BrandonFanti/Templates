from django.urls import path

from . import views, app_name

urlpatterns = [
    path("",  views.index, name=app_name),
    path("/", views.index, name=app_name),
    path("login", views.user_login, name=app_name),
]