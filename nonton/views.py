from django.shortcuts import render


from .models import Post

def index(request):
    posts = Post.objects.all()

    playliest = Post.objects.values('playlist').distinct()

    context = {
        'title': 'Nonton | txtdrustadz Channel',
        'heading': 'Kumpulan kajian dari para guru-guru kita',
        'subheading': 'txtdrustadz Channel hadir bersama mengatasi masalah dikeseharian kita',
        'Playliest': playliest,
        'Posts': posts,
    }
    return render(request, 'nonton/index.html', context)


def playlistPost(request, playlistInput):
    posts = Post.objects.filter(playlist=playlistInput)

    playliest = Post.objects.values('playlist').distinct()

    context = {
        'title': 'Playlist | txtdrustadz Channel',
        'heading': 'Kumpulan kajian dari para guru-guru kita',
        'Playliest': playliest,
        'Posts': posts,
    }
    return render(request, 'nonton/playlist.html', context)

def detailPost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)

    playliest = Post.objects.values('playlist').distinct()

    context = {
        'title': 'Slug | txtdrustadz Channel',
        'heading': 'Kumpulan kajian dari para guru-guru kita',
        'Playliest': playliest,
        'Posts': posts,
    }
    return render(request, 'nonton/detail.html', context)
