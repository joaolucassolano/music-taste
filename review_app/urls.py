from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('artists', views.ArtistList.as_view()),
    path('artists/<int:pk>', views.ArtistDetail.as_view()),
    path('musics', views.MusicList.as_view()),
    path('musics/<int:pk>', views.MusicDetail.as_view()),
    path('reviews', views.ReviewList.as_view()),
    path('reviews/<int:pk>', views.ReviewDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)