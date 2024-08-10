from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_music_piece, name='add_music_piece'),
    path('list/', views.list_music_pieces, name='list_music_pieces'),
    path('history/', views.project_history, name='project_history'),
    # Удалите или измените следующую строку, если вам больше не нужна отдельная страница для деталей
    # path('detail/<int:id>/', views.detail_music_piece, name='detail_music_piece'),
]
