from django.shortcuts import render

# Create your views here.
def add_server(request):
    return render(request, 'servers/add_server.html', {})