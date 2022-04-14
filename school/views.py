from django.shortcuts import render


def home(request):
    return render(request, 'school/home.html')
# Create your views here.
