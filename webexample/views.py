from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h3>Пример простого текстового сообщения </br> \
    <font color=red>....новости информационных технологий</font></br> \
    </h3>")
# Create your views here.
