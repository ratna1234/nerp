from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
	return HttpResponse('This is an Index Page')
# Create your views here.
