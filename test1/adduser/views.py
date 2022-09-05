from django.shortcuts import render,redirect
from . models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def showRegistration(request):
    if request.method == 'POST':
        u = User()
        u.username = request.POST.get('uname')
        u.email = request.POST.get('em')
        u.password = make_password(request.POST.get('pw'))
        if u.username =='' or u.email == '' or u.password == '':
            return render(request,'addduser/adduser.html')
        else:
            u.save()
            return redirect('adduser')
    else:
        return render(request, 'addduser/adduser.html')
    