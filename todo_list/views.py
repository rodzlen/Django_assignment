from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse
from django.views.decorators.http import require_http_methods

from todo_list.form import  TodoUpdateForm
from todo_list.models import Todo
# Create your views here.
def todo_list(request):
    todos = Todo.objects.all().order_by('-created_at')
    context = {"todos":todos}
    return render(request, 'todo_list.html',context)

def todo_info(request,pk):
    todo = get_object_or_404(Todo, pk=pk)
    context = {
        "todo": todo
    }
    return render(request, 'todo_detail.html',context)

@require_http_methods(['GET',"POST"])
def todo_create(request):
    form =TodoUpdateForm(request.POST or None)

    if form.is_valid():
        todo= form.save(commit=False)
        todo.user = request.user
        todo.save()


        return redirect(reverse('todo_list'))

    context = {"form":form}
    return render(request, 'todo_create.html', context)

@require_http_methods(['GET',"POST"])
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoUpdateForm(request.POST or None, instance=todo, is_update=True)
    if form.is_valid():
        todo = form.save()
        return redirect(reverse('todo_detail',kwargs={"pk":todo.id}))
    context = {'form':form}
    return render(request, 'todo_update.html',context)
@login_required()
@require_http_methods(['POST'])
def todo_delete(request,pk):
    print(request.user)
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if todo:
        todo.delete()
        return redirect(reverse('todo_list'))





