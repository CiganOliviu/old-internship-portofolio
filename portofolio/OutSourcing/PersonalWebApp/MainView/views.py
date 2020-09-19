from django.shortcuts import render

def Index(request):
    return render(request, 'views/index.html')

def Books(request):
    return render(request, 'views/books.html')