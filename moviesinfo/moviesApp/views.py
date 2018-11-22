from django.shortcuts import render
from . import form
from .models import AddMoviesModel

# Create your views here.
def moviesInfo(request):
    return render(request,'moviesApp/index.html')

def AddViews(request):
    forms=form.AddMovies()
    if request.method=='POST':
        forms=form.AddMovies(request.POST)
        if forms.is_valid():
            forms.save(commit=True)
            return render(request,'moviesApp/index.html')
    return render(request,'moviesApp/add.html',{'forms':forms})
def listViews(request):
    list=AddMoviesModel.objects.all()
    return render(request,'moviesApp/list.html',{'list':list})
