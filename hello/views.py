from django.shortcuts import render
from .models import Person

def Main(request):
    all = Person.objects.all()
    return render(request, 'main.html', {'Person':all})
def Hello(request):
    return render(request, 'hello.html')

