from . import views
from django.urls import path, re_path
from django.conf.urls import include, url

urlpatterns = [
   # Song Url
   path('', views.ManageSongListView.as_view(), name='manageSong'),
   path('createSong', views.CreateSong.as_view(), name='createSong'),
   path('editSong/<int:pk>', views.EditSong.as_view(), name='editSong'),
   path('deleteSong/<int:pk>', views.DeleteSong.as_view(), name='deleteSong'),
   path('songSerachView', views.SearchSong.as_view(), name='songSerachView'),
   

   # Podcast Url
   path('managePodCast', views.ManagePodcastListView.as_view(), name='managePodCast'),
   path('createPodcast', views.CreatePodcast.as_view(), name='createPodcast'),
   path('editPodcast/<int:pk>', views.EditPodcast.as_view(), name='editPodcast'),
   path('deletePodcast/<int:pk>', views.DeletePodcast.as_view(), name='deletePodcast'),
   path('serachPodcast', views.SearchPodcast.as_view(), name='serachPodcast'),


   # Audiobook Url
   path('manageAudioBook', views.ManageAudioBookListView.as_view(), name='manageAudioBook'),
   path('createAudioBook', views.CreateAudioBookView.as_view(), name='createAudioBook'),
   path('editAudioBook/<int:pk>', views.EditAudioBook.as_view(), name='editAudioBook'),
   path('deleteAudioBook/<int:pk>', views.DeleteAudioBookView.as_view(), name='deleteAudioBook'),
   path('serachAudioBook', views.SearchAudioBook.as_view(), name='serachAudioBook'),
]

