from django.shortcuts import render

# Create your views here.

def index(request):
    data = {}
    data['login'] = False
    if request.method == 'POST':
        if request.POST['login'] == 'admin' and request.POST['password'] == 'teste':
            data['login'] = True
            return render(request, 'app/index.html', data)
        else:
            data['login'] = False
            return render(request, 'app/index.html', data)
    return render(request, 'app/index.html', data)