"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from music import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_album_list, name='post-album-list'),
    path('music/<int:pk>', views.album_detail, name='album-detail'),
    path('music/add-album', views.add_album, name='add-album'),
    path('music/<int:pk>/delete', views.delete_album, name='delete-album'),
    path('music/<int:pk>/edit', views.edit_album, name='edit-album'),
    path('artist/<int:pk>', views.albums_by_artist, name="albums-artist"),
    path('artists', views.artist_list, name="artist-list"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)