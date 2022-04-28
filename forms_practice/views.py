from django.shortcuts import render
from .forms  import UserForm
from django.http import HttpResponse
def loginView(req):
    return render(req,"login.html")

def loggedView(req):
    username='not logged in'
    password='not logged in'
    if req.method=='POST':
        form=UserForm(req.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
    return render(req,'loggedin.html',{'username':username,'password':password})

def sessionloggedView(req):
    username='not logged in'
    password='not logged in'
    if req.method=='POST':
        form=UserForm(req.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            req.session['username']=username
            req.session['password']=password
    return render(req,'loggedin.html',{'username':username,'password':password})

def sessionloginView(req):
    if req.session.has_key('username') and req.session.has_key('password'):
        return render(req,'loggedin.html',{'username':req.session['username'],'password':req.session['password']})
    else:
        return render(req,'login.html')

def sessionLogoutView(req):
    try:
        del req.session['username']
        del req.session['password']
    except:
        pass
    return HttpResponse("<h1>LoggedOut</h1>")
