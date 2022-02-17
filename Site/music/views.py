from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView, TemplateView


def music_home(request):
    music = Articles.objects.order_by('-date')
    return render(request, 'music/music_home.html', {'music': music})


class MusicDetailView(DetailView):
    model = Articles
    template_name = 'music/details_view.html'
    context_object_name = 'article'


class MusicUpdateView(UpdateView):
    model = Articles
    template_name = 'music/create.html'
    Articles.objects.all().delete()
    media = Articles.objects.all()
    for audio in media:
        audio.delete()

    form_class = ArticlesForm


class MusicDeleteView(DeleteView):
    model = Articles
    success_url = '/music/'
    template_name = 'music/music-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка!'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'music/create.html', data)