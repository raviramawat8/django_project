from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'app1/index.html')
def about(request):
    return render(request,'app1/about.html')
def login(request):
    return render(request,'app1/login.html')
def signup(request):
    return render(request,'app1/signup.html')
def sign(request):
    try:
        if request.method == "POST":
            form = Signup(request.POST)

            if form.is_valid():
                return HttpResponse("Success")
            else:
                return HttpResponse("Failure")
        else:
            return HttpResponse("Incorrect Method")
    except Exception as e:
        return (e)
