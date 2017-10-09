# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	data = {
		"things": [
			"one",
			"two",
			"three"
		]
	}

	return render(request, "bullet/index.html", data)

def taskfeed(request):
	return render(request, "bullet/taskfeed.html")

def login(request):
	return render(request, "bullet/login.html")

def newtask(request):
	return render(request, "bullet/newtask.html")
