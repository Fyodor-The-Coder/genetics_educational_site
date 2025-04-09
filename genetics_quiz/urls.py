from django.urls import path
from genetics_quiz.views import *

urlpatterns = [
    path('start/', start_quiz, name='start_quiz'),
    path('begin/', begin_quiz, name='begin_quiz'),
    path('quiz/', quiz, name='quiz'),
    path('results/', results, name='results'),
]