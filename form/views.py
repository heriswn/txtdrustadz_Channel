from django.shortcuts import render
from .forms import ContactForm

def index(request):

    contact_form = ContactForm()

    context = {
        'title': 'Form | txtdrustadz Channel',
        'heading': 'Form',
        'form':contact_form,
    }

    if request.method == 'POST':
        print('This is POST method')
        context['name'] = request.POST['name']
        context['email'] = request.POST['email']
    else:
        print('This is GET method')

    return render(request, 'form/index.html', context)
