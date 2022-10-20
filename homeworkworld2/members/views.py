from cProfile import label
import numbers
from webbrowser import get
from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from pkg_resources import require
from django.urls import reverse

class world(forms.Form):
    task1 = forms.CharField(label="Pls enter your username", min_length= 5, max_length= 20)
    task2 = forms.IntegerField(label="Pls enter your age", max_value= 13)

turudek = ["satu", "dua", "tiga"]
age = []
def func1(request):
    if request.method== "POST":
        input = world(request.POST)
        if input.is_valid():
            mylist = input.cleaned_data["task1"]
            mylist1 = input.cleaned_data["task2"]
            turudek.append(mylist)
            age.append(mylist1)
            return HttpResponseRedirect(reverse("Second2"))
        else:
            return render(request, "membersfile1.html", {"list": turudek, "list2": age})
    return render(request, "membersfile1.html", {"form": world(), "list": turudek, "list2": age})

def func2(request):
    return render(request, "membersfile2.html", {"list": turudek, "list2": age})
# Create your views here.

def func3(request):
    if "task1" not in request.session:
        request.session["task1"]= []
    if "task2" not in request.session:
        request.session["task2"]= []

    return render(request, "membersfile2.html", {"list": request.session["task1"], "list2": request.session["task2"]})

def func4(request):
    if request.method== "POST":
        input1 = world(request.POST)
        if input1.is_valid():
            mylist1 = input1.cleaned_data["task1"]
            request.session["task1"] += [mylist1]
            mylist2 = input1.cleaned_data["task2"]
            request.session["task2"] += [mylist2]
            return HttpResponseRedirect(reverse("Third3"))
        else:
            return render(request, "membersfile3.html", {"form": input1})
    return render(request, "membersfile3.html", {"form": world()})
