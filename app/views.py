from django.shortcuts import render

# Create your views here.
import datetime

def built_in_filters(request):
    dt=datetime.datetime.now()
    d={'data':'tHIS is WEEkEnd','c':4,'dt':dt}

    return render(request,'built_in_filters.html',d)

