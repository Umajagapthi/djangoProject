from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    res=HttpResponse("""<html><body bgcolor="pink">
    <center><h1>peace in a day make smile in your face</h1></center> </body></html>""")
    return res