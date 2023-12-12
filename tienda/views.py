from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.db.models import Q

from django.contrib import messages

from .models import *


# Create your views here.

def index(request):
    return render(request, "index.html")


def collage(request):
    return render(request, "collage.html")