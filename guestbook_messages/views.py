from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def message_board(request):
    return render(request, 'message_board.html')
