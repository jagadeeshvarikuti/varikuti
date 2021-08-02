from django.shortcuts import render
from .models import * 

# Create your views here.
def home(request):
	ps = studentaddress1.objects.all()
	context = {'ps':ps}
	return render (request,"index.html",context)