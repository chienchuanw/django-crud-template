from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from tasks.models import Task
from django.contrib import messages


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "tasks/index.html")


def add(request: HttpRequest) -> HttpResponse:
    if request.POST:
        task = Task()
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.save()

        messages.success(request, "創建成功")
        return redirect("tasks:add")

    return render(request, "tasks/add.html")
