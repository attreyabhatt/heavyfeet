from django.shortcuts import render,redirect
from dailytasks.models import UserTask
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def task_view(request):
    if request.method == "POST":
        current_task = request.POST['addtask']
        UserTask(task_name=current_task).save()

    task_qs = UserTask.objects.all().order_by('completed','id')
    context = {
        'task_qs':task_qs,
    }
    return render(request,"tasks/task.html",context)

@login_required
def task_handle_view(request,task_id):
    current_task = UserTask.objects.get(id=task_id)
    
    if request.method == "POST":
        isDelete = request.POST.get('delete_task', False)
        isComplete = request.POST.get('complete_task', False)
        if isDelete:
            current_task.delete()
        elif isComplete:
            current_task.completed = True
            current_task.save()
        
    
    return redirect("tasks")