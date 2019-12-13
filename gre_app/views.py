# gre views 
from django.shortcuts import HttpResponseRedirect, render

def index(request):
    '''
    Renders home page
    '''
    context = {}
    return render(request, 'home.html', context)

