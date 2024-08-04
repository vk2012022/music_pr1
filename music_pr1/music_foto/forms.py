from django import forms
from .models import MusicPiece

class MusicPieceForm(forms.ModelForm):
    class Meta:
        model = MusicPiece
        fields = ['title', 'photo', 'audio', 'description']
