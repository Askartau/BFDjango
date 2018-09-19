from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
import datetime


def todo_list(request):
    tasks = list()

    task1 = Task()
    task1.name = "task1"
    task1.created = '10.09.2018'
    task1.due_on = '12.09.2018'
    task1.owner = 'Ádmin'

    task2 = Task()
    task2.name = "task2"
    task2.created = '10.09.2018'
    task2.due_on = '12.09.2018'
    task2.owner = 'Ádmin'

    task3 = Task()
    task3.name = "task3"
    task3.created = '10.09.2018'
    task3.due_on = '12.09.2018'
    task3.owner = 'Ádmin'

    task4 = Task()
    task4.name = "task4"
    task4.created = '10.09.2018'
    task4.due_on = '12.09.2018'
    task4.owner = 'Ádmin'

    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)
    tasks.append(task4)

    context = {
        'tasks': tasks,
    }
    return render(request, 'main/todo.html', context)

def done_list(request):
    dones = list()

    Task1 = Task()
    Task1.name = "task4"
    Task1.created = '10.09.2018'
    Task1.due_on = '12.09.2018'
    Task1.owner = 'Ádmin'
    Task1.mark = True

    Task2 = Task()
    Task2.name = "task4"
    Task2.created = '10.09.2018'
    Task2.due_on = '12.09.2018'
    Task2.owner = 'Ádmin'
    Task2.mark = True


    Task3 = Task()
    Task3.name = "task4"
    Task3.created = '10.09.2018'
    Task3.due_on = '12.09.2018'
    Task3.owner = 'Ádmin'
    Task3.mark = True

    Task4 = Task()
    Task4.name = "task4"
    Task4.created = '10.09.2018'
    Task4.due_on = '12.09.2018'
    Task4.owner = 'Ádmin'
    Task4.mark = True

    dones.append(Task1)
    dones.append(Task2)
    dones.append(Task3)
    dones.append(Task4)

    context ={
        'dones': dones,
    }
    return render(request, 'main/done.html', context)



