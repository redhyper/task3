from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')
def dudos(request):
    return render(request, 'mainApp/popuga.html')
# Create your views here.
