from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        return Response({"these": "test"})
