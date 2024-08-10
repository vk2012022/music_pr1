from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_music_piece, name='add_music_piece'),
    path('list/', views.list_music_pieces, name='list_music_pieces'),
    path('detail/<int:id>/', views.detail_music_piece, name='detail_music_piece'),
    path('history/', views.project_history, name='project_history'),
    path('scroll/', views.scroll_music_pieces, name='scroll_music_pieces'),
    path('edit/<int:id>/', views.edit_music_piece, name='edit_music_piece'),  # Маршрут для редактирования произведения
]

