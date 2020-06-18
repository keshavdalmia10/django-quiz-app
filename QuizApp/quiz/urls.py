from django.urls import path,include
from rest_framework.routers import DefaultRouter
from quiz import views
from quiz.views import SaveUsersAnswer,UsersAnswerSerializer



router=DefaultRouter()
router.register('Quiz',views.QuizViewSet)
router.register('Questiondetail',views.QuestionDetailViewset)

urlpatterns=[
    path('',include(router.urls)),
    path("save-answer/", SaveUsersAnswer.as_view()),
]
