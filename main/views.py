from django.shortcuts import render, redirect
from django.http import HttpResponse
from main import models
from django.contrib.auth.decorators import login_required
from main.forms import Urlform
import random

# Create your views here.
@login_required
def fetch_private(request, model, url):
    print('\n\n\nreached here tooooo\n\n\n')
    actual_url = model.actual_url
    model.num_clicks += 1
    model.save()
    return None

def fetch(request, url):
    try:
        model = models.Database.objects.get(shortened_url = url)
    except:
        return render(request, 'notfound.html')

    if model.is_private :
        if request.user.is_authenticated :
            actual_url = model.actual_url
            model.num_clicks += 1
            model.save()
            return redirect(actual_url)
        else:
            print('\n\n\nreached here\n\n\n')
            return fetch_private(request, model, url)
    actual_url = model.actual_url
    model.num_clicks += 1
    model.save()
    return redirect(actual_url)
    
def generate_random():
    short_url = ""
    for i in range(5):
        x = random.randint(65, 90)
        y = random.randint(97, 122)
        ch = random.randint(1,2)
        if ch == 1:
            short_url += chr(x)
        else :
            short_url += chr(y)
    return short_url

def get_url(request):
    context = {}
    urlform = Urlform()
    short_url = ""
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        urlform = Urlform(request.POST)
        # check whether it's valid:
        if urlform.is_valid():
            model = models.Database()
            if urlform.cleaned_data['shortened_url']:
                short_url = urlform.cleaned_data['shortened_url']
                if short_url.__contains__('/'):
                    urlform.errors['shortened_url'] = ['can contain only alphabets, numbers and "_" ']
                else:
                    model.shortened_url = short_url
                    model.actual_url = urlform.cleaned_data['actual_url']
                    model.is_private = urlform.cleaned_data['is_private']
                    context['short_url']= 'localhost:8000/' + short_url
                    model.save()
            else: 
                short_url = generate_random()
                try:
                    while model.objects.get(shortened_url = short_url):
                        short_url = generate_random()
                except:
                    pass
            
                model.shortened_url = short_url
                model.actual_url = urlform.cleaned_data['actual_url']
                model.is_private = urlform.cleaned_data['is_private']
                context['short_url']= 'localhost:8000/' + short_url
                model.save()
    
    context['form'] = urlform
    return render(request, 'index.html',context)