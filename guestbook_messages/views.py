from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def messageboard(request):
    return render(request, 'messageboard.html')

def createmessageboard(request):
    return render(request, 'createmessageboard.html')
