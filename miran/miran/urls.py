from django.contrib import admin
from django.urls import path, include

from users import views

urlpatterns = [
    path('', views.home, name="home"),
    path('users/', include('users.urls', namespace='users')),
    path('books/', include('books.urls', namespace='books')),
    path('admin/', admin.site.urls),
]
