from quiz.models import Quiz,Question, Answer, UsersAnswer
from rest_framework import serializers

class QuizListSerializer(serializers.ModelSerializer):
    questions_count=serializers.SerializerMethodField()
    class Meta:
        model=Quiz
        fields = ["id", "name", "slug", "questions_count"]
        read_only_fields=["questions_count"]

    def get_questions_count(self,obj):
        return obj.question_set.all().count()

class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=["id","question","label"]
class QuestionSerializers(serializers.ModelSerializer):
    answer_set=AnswerSerializers(many=True)
    class Meta:
        model=Question
        fields="__all__"
class UsersAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsersAnswer
        fields="__all__"