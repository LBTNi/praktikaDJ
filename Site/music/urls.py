from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.music_home, name='music_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.MusicDetailView.as_view(), name='music-detail'),
    path('<int:pk>/update', views.MusicUpdateView.as_view(), name='music-update'),
    path('<int:pk>/delete', views.MusicDeleteView.as_view(), name='music-delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)