from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

def index(request):
    return HttpResponse("Hello, world. You're at the youscrape index.")

# Create your views here.
@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        return Response({"these": "test"})


