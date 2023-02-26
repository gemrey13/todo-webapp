from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import *
# Create your views here.

def index(request):
	tasks_todo = Task.objects.filter(status='todo')
	tasks_ongoing = Task.objects.filter(status='ongoing')
	tasks_finished = Task.objects.filter(status='finished')

	if request.method == "POST":
		title = request.POST['title']
		todo = Task.objects.create(title=title)
		return redirect('index')

	return render(request, 'mainApp/index.html', {
		'tasks_todo': tasks_todo,
		'tasks_ongoing': tasks_ongoing,
		'tasks_finished': tasks_finished
		})


def update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
    	status = request.POST['status']
    	if status == 'ongoing':
    		task.status = 'ongoing'
    	elif status == 'finished':
    		task.status = 'finished'
    	elif status == 'todo':
    		task.status = 'todo'
    	task.save()
    	return redirect('index')


def delete(request, pk):
	task = get_object_or_404(Task, pk=pk)
	task.delete()
	return redirect('index')
