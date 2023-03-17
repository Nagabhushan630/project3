from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def naga(request):
    return HttpResponse('<h1>my nama is naga</h1>')