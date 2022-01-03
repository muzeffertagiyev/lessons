from django.shortcuts import render

import datetime

# Create your views here.


def new_year(request):
    now=datetime.datetime.now()
    return render(request,"new_year/index.html",{"newyear":now.month==1 and now.day==1})

