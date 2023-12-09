from django.urls import path

from . import views

app_name = 'signs'


urlpatterns = [
    path("change_sign/", views.change_signs, name="change_sign"),
    path("create_sign/", views.create_sign, name="create_sign"),
]
