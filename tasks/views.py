from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from tasks.models import Task
from django.contrib import messages


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()

    context = {"tasks": tasks}

    return render(request, "tasks/index.html", context)


def add(request: HttpRequest) -> HttpResponse:
    if request.POST:
        task = Task()
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.save()

        messages.success(request, "創建成功")
        return redirect("tasks:add")

    return render(request, "tasks/add.html")


def detail(request: HttpRequest, id: int) -> HttpResponse:
    task = get_object_or_404(Task, id=id)
    context = {"task": task}

    return render(request, "tasks/detail.html", context)
