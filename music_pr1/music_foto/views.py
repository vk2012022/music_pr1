from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MusicPiece
from .forms import MusicPieceForm

def home(request):
    return render(request, 'music_foto/home.html')

def add_music_piece(request):
    if request.method == 'POST':
        form = MusicPieceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Произведение успешно добавлено.")
            return redirect('list_music_pieces')
        else:
            messages.error(request, "Произошла ошибка при добавлении произведения. Пожалуйста, проверьте введенные данные.")
    else:
        form = MusicPieceForm()
    return render(request, 'music_foto/add_music_piece.html', {'form': form})

def list_music_pieces(request):
    music_pieces = MusicPiece.objects.all()
    return render(request, 'music_foto/list_music_pieces.html', {'music_pieces': music_pieces})

def detail_music_piece(request, id):
    music_piece = get_object_or_404(MusicPiece, id=id)
    return render(request, 'music_foto/detail_music_piece.html', {'music_piece': music_piece})
