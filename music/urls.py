from django.urls import path, re_path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    re_path(r'^$', views.IndexView.as_view(), name="index"),

    # /music/123/
    #re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail")
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),

    # /music/album/add
    path('album/add', views.AlbumCreate.as_view(), name='album-add'),
]