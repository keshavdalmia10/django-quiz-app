from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from quiz.models import Answer, Question
from quiz.serializers import QuizListSerializer, QuizListSerializer,QuestionSerializers,UsersAnswerSerializer,resultserializers
from rest_framework import viewsets
from . import models
from quiz.models import UsersAnswer,result,Quiz
class QuizViewSet(viewsets.ModelViewSet):

    serializer_class =  QuizListSerializer
    queryset = models.Quiz.objects.all()

class QuestionDetailViewset(viewsets.ModelViewSet):

    serializer_class=QuestionSerializers
    queryset=models.Question.objects.all()


class SaveUsersAnswer(generics.UpdateAPIView):
    serializer_class=UsersAnswerSerializer
    queryset=models.UsersAnswer.objects.all()

class Resultview(generics.GenericAPIView):
    serializer_class=resultserializers

    def post(self, request, *args, **kwargs):
#        result_id = request.data['result']
#        question_id = request.data['question']
#        answer_id = request.data['answer']

        Result = get_object_or_404(result, id=1)
        question = get_object_or_404(Question, id=1)

        quiz = Quiz.objects.get(slug=self.kwargs['slug'])




        correct_answers = 0

        for users_answer in UsersAnswer.objects.all():
            answer = Answer.objects.get(question=users_answer.question, is_correct=True)
            print(answer)
            print(users_answer.answer)
            if users_answer.answer == answer:
                correct_answers += 1

        Result.score =  correct_answers
        print(Result.score)
        Result.save()

        return Response(self.get_serializer(quiz).data)
