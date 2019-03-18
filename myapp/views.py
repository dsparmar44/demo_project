from django.shortcuts import render

# Create your views here.
def index (request):
 
	return render(request,'d.html')
	
def home(request):
    return render(request,'DD.html')
	
	
