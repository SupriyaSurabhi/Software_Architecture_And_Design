
from django.shortcuts import render
from django.http import JsonResponse
def index(request):
    #We will access  the Model Objects and use templates to prepare responses.
    return JsonResponse({"Message":"Hello World!"})
# Create your views here

