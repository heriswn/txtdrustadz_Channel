from django.shortcuts import render


def index(request):
    context = {
        'title': 'Nonton | txtdrustadz Channel',
        'heading': 'Kumpulan kajian dari para guru-guru kita',
        'subheading': 'txtdrustadz Channel hadir bersama mengatasi masalah dikeseharian kita',
    }
    return render(request, 'nonton/index.html', context)
