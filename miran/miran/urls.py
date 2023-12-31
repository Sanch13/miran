from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users import views

urlpatterns = [
    path('', views.home, name="home"),
    path('users/', include('users.urls', namespace='users')),
    path('books/', include('books.urls', namespace='books')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
