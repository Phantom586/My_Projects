from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html', {})

def graphic_db(request):

    
    return render(request, 'db_app/index.html', {})

