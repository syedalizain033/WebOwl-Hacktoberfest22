from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import is_valid_path
from webowl import forms
# Create your views here.

def home(request):
    form = forms.SearchWeb(request.POST or None)
    if request.method=='GET':

        return render(request, 'webowl/home.html', {'form':form})
    if request.method=='POST':
        if form.is_valid():
            web=form.cleaned_data['url']
            import os
            resp=os.popen('curl -I '+web)
            resp=resp.read()
            return render(request, 'webowl/home.html',{'url':resp, 'form':form})

def red(request):
    return redirect('home/')