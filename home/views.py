from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoCreateForm , TodoUpdateForm
from django.contrib import messages



def home_page(request):
    all = Todo.objects.all
    #return HttpResponse("god help me and soon i can enshaakllah")
    return render(request,'home.html',{'khar' : all })


def say_hello(request):
    #return HttpResponse("god help me and soon i can enshaakllah")
    person={'name':'foroozan'}
    return render(request,'hello.html' , context=person)


def detail(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    return render(request,'detail.html' ,{'todo' : todo})
# Create your views here.

def delete(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'task is deleteed successfuly' , 'success')
    return redirect('home')

def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            Todo.objects.create(title=cd['title'], body =cd['body'], created=cd['created'] )
            messages.success(request, 'task created successfuly' , 'warning')
            return redirect('home')   
    else:
        form = TodoCreateForm()
        return render(request , 'create.html' , {'form': form })

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form=TodoUpdateForm(request.POST , instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'task updated successfuly' , 'danger')
            return redirect('details' , todo_id)

    else :
        form = TodoUpdateForm(instance=todo)
        return render(request , 'update.html' , {'form': form })
