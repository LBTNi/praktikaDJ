from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'full_text', 'date', 'audio']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'гг-дд-мм часы:минуты:секунды'
            }),
            "full_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "audio": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите файл расширения .mp3',
            }),
        }