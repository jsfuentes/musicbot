from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([str(q.id) + ". " + q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged

# # Create your views here.
# @api_view(['GET'])
# def post_collection(request):
#     if request.method == 'GET':
#         return Response({"these": "test"})


