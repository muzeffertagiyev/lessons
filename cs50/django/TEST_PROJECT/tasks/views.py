from django.shortcuts import render

# Create your views here.


def tasks(request):
    tasks=["foo","bar",1]
    return render(request,"tasks/tasks.html",{
        "tasks":tasks
    })


def add(request):

    return render(request,"tasks/add.html")