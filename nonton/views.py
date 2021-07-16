from django.shortcuts import render


from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'title': 'Nonton | txtdrustadz Channel',
        'heading': 'Kumpulan kajian dari para guru-guru kita',
        'subheading': 'txtdrustadz Channel hadir bersama mengatasi masalah dikeseharian kita',
        'Posts': posts,
    }
    return render(request, 'nonton/index.html', context)
