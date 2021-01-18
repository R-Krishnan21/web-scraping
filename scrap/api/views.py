from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import QuestionsSerializers
from .models import Questions
from .scrap import scrape

# Create your views here.

def index(requests):
    return HttpResponse("Success")

class Question(viewsets.ViewSet):
    def list(self, request):
        queryset = Questions.objects.all()
        serializer = QuestionsSerializers(queryset, many=True)
        return Response(serializer.data)

def latest(request):
    try:
        data = scrape()
        try:
            for data in data:
                Questions.objects.create(
                    question = data['question'],
                    detail = data['detail'],
                    votes = data['votes'],
                    link = data['link'],
                    views = data['views'],
                    tags = data['tags']
                )
            return HttpResponse("<h1>ok<h1>")
        except Exception as e:
            return HttpResponse("<h1>{}<h1>".format(e))
    except Exception as e:
        return HttpResponse("<h1>{}<h1>".format(e))