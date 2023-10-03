from django.shortcuts import render , redirect
from .forms import UserRegestrationForm , UserLoginForm
from django.contrib.auth.models  import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout


def user_register(request):
    #return HttpResponse("rejester form")
    if request.method =='POST':
        form=UserRegestrationForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=User.objects.create_user(cd['username'],cd['email'],cd['password'],)
            user.first_name = cd['first']
            user.first_name = cd['last']
            user.save()
            messages.success(request, 'regesteration done successfuly . . .' , 'Primary')
            return redirect('home')

    else:
        form=UserRegestrationForm()
    return render(request , 'register.html' , {'form': form })
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request , username = cd['username'], password = cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request, 'logged in successfuly .', 'success')  #Secondary
                return redirect('home')
            else:
                messages.error(request, 'username or password is wrong', 'danger')
    else:
        form=UserLoginForm()

    return render(request , 'login.html' , {'form' : form})


def user_logout(request):
    logout(request)
    messages.success(request, 'logged out successfuly .', 'Secondary')  #Secondary
    return redirect('home')
