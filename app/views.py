from django.shortcuts import render

# Create your views here.
def nature(request):
    return render(request,'static.html')