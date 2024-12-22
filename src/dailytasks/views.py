from django.shortcuts import render,redirect
from dailytasks.models import UserTask
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def task_view(request):
    if request.method == "POST":
        current_task = request.POST['addtask']
        UserTask(user=request.user,task_name=current_task).save()

    task_qs = UserTask.objects.filter(user=request.user).order_by('completed','id')
    number_of_tasks_completed = 0
    for task in task_qs:
        if task.completed == True:
            number_of_tasks_completed += 1

    context = {
        'task_qs':task_qs,
        'number_of_tasks_completed':number_of_tasks_completed,
    }
    return render(request,"tasks/task.html",context)

@login_required
def task_handle_view(request,task_id):
    current_task = UserTask.objects.get(id=task_id)
    
    if current_task.user == request.user:
        if request.method == "POST":
            isDelete = request.POST.get('delete_task', False)
            isComplete = request.POST.get('complete_task', False)
            if isDelete:
                current_task.delete()
            elif isComplete:
                current_task.completed = True
                current_task.save()
    return redirect("tasks")