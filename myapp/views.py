from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'homepage.html')

def login(request):
    return render(request, 'loginproject.html')

def form(request):
    return render(request, 'form.html')

def words(request):
    text = request.POST['text']
    num_of_words = len(text.split())
    return render(request, 'words.html', {'num':num_of_words})