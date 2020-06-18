from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from quiz.models import Answer, Question
from quiz.serializers import QuizListSerializer, QuizListSerializer,QuestionSerializers,UsersAnswerSerializer
from rest_framework import viewsets
from . import models
from quiz.models import UsersAnswer
class QuizViewSet(viewsets.ModelViewSet):

    serializer_class =  QuizListSerializer
    queryset = models.Quiz.objects.all()

class QuestionDetailViewset(viewsets.ModelViewSet):

    serializer_class=QuestionSerializers
    queryset=models.Question.objects.all()
class SaveUsersAnswer(generics.UpdateAPIView):
    serializer_class=UsersAnswerSerializer
    queryset=models.UsersAnswer.answer
    
