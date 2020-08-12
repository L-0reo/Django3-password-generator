from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = list('ABCDEFGHIJKLNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    special = list('~!@#$%^&*')
    length = int(request.GET.get('length'))
    thepassword =''

    if request.GET.get('uppercase'):
        characters.extend(uppercase)
    if request.GET.get('numbers'):
        characters.extend(numbers)
    if request.GET.get('special'):
        characters.extend(special)

    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html', {'password':thepassword})
