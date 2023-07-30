from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
def funct_logement(request):
    if request.method == 'POST':
        fm = Register_log(request.POST)
        if fm.is_valid():
            fm.save() 
    else:
        fm = Register_log()
    return render(request, 'systeme_U/logement.html',{'form':fm})

