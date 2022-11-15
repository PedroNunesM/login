from django.shortcuts import render
import os
# Create your views here.

def index(request):
    data = {}
    data['login'] = False
    data['tentativa'] = False
    if request.method == 'POST':
        if request.POST['login'] == os.environ['SITE_USER'] and request.POST['password'] == os.environ['SITE_PASS']:
            data['login'] = True
            data['tentativa'] = False
            return render(request, 'app/index.html', data, status=200)
        else:
            data['login'] = False
            data['tentativa'] = True
            return render(request, 'app/index.html', data, status=400)
    return render(request, 'app/index.html', data)