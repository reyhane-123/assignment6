from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

list1=[
    {"id":1,"name":"class_python"},
    {"id":2,"name":"class_html"},
    {"id":3,"name":"class_jango"},
    {"id":4,"name":"class_c#"}
]

def khata(request):
    id=request.GET.get('id',0)
    for item in list1:
        if item['id'] in list1:
            return render(request,'khata/doree.html')
        else:
            return render(request,'khata/test.html')
