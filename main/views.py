from django.shortcuts import render, redirect
from django.http import HttpResponse
from main import models
from main.forms import Urlform
import random

# Create your views here.
def fetch(request, url):
    model = models.database.objects.get(shortened_url = url)
    model.num_clicks += 1
    model.save()
    return redirect(model.actual_url)
    
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

# def store(request):
#     if request.method == 'POST':
#         model = models.database()
#         short_url = generate_random()
#         try:
#             while model.objects.get(shortened_url = short_url):
#                 short_url = generate_random()
#         except:
#             pass
        
#         model.shortened_url = short_url
#         model.actual_url = request.POST.get('url')
#         model.save()

#         return HttpResponse(short_url)
#     return render(request, 'index.html')

def get_url(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Urlform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try :
                obj = models.database.objects.get(actual_url = form.cleaned_data['url'])
                return  HttpResponse(obj.shortened_url)
            except:
                model = models.database()
                short_url = generate_random()
                try:
                    while model.objects.get(shortened_url = short_url):
                        short_url = generate_random()
                except:
                    pass
                
                model.shortened_url = short_url
                model.actual_url = form.cleaned_data['url']
                model.save()

            return HttpResponse(short_url)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Urlform()

    return render(request, 'index.html', {'form': form})