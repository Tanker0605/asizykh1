#from django.shortcuts import render

# Create your views here.
from .models import *
from django.shortcuts import render
def index(request):
    bbs = Bb.objects.all()
    rs = Rubric.objects.all()
    return render(request, "btest/index.html", {'bbs': bbs, 'rs': rs})


