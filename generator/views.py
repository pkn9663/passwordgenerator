"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def password(request):
    """Stores the password"""
    assert isinstance(request, HttpRequest)
    chars = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numeric'):
        chars.extend(list('1234567890'))
    if request.GET.get('symbols'):
        chars.extend(list('!@#$%^&*'))
    length = int(request.GET.get('length', 10))

    passgen = ''

    for i in range(length):
        passgen += random.choice(chars)
    return render(
        request,
        'app/password.html', {'password': passgen}
        )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Praveen Kumar N',
            'message':'This is the first Django webpage to create Password',
            'year': datetime.now().year,
        }
    )
