from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(Request):

    # return HttpResponse("hello binaries")
    return render(Request,'index.html')