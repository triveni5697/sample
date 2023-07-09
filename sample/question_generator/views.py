from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import generics

from .models import *

from .serializers import QuestionSerializer

def exam_view(request):
    data=Question.objects.all()
    #choices = Choice.object.all()
    #for i in da:
        #data=Question.objects.filter(id=i.id)
        #choices= Choice.objects.filter(question=i.id)
    return render(request, '.\\rest_framework\\api.html',{'data':data})
class QuestionListAPIView(APIView):

    queryset = Question.objects.all()

    serializer_class = QuestionSerializer
    
    '''
    def get(self, request):

        detail = [ {"text": Question.text} for detail in Question.objects.all()]

        return Response(detail)

  

    def post(self, request):

  

        serializer = QuestionListAPIView(data=request.data)

        if serializer.is_valid(raise_exception=True):

            serializer.save()

            return  Response(serializer.data)

'''
