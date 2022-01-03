from django.shortcuts import render
from django import forms

# Create your views here.

class NewTaskForm(forms.Form):

    tasks=forms.CharField(label="New task")


tasks=[]
def index(request):
    
    
    return render(request,"tasks/tasks.html",{
        "tasks":tasks
    })


def add(request):
    if request.method=="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data["tasks"]
            tasks.append(task)
        else:
            return render(request,"tasks/add.html",{
                "form":form
            })

    return render(request,"tasks/add.html",{
        "form":NewTaskForm()
    })