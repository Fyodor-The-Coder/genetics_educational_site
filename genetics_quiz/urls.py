"""
URL-маршруты приложения 'genetics_quiz'.

Доступные пути:
- /start/ - стартовая страница квиза
- /quiz/ - страница непосредственно самого квиза
- /results/ - страница результатов квиза
"""

from django.urls import path
from genetics_quiz.views import start_quiz, begin_quiz, quiz, results

urlpatterns = [
    path('start/', start_quiz, name='start_quiz'),
    path('begin/', begin_quiz, name='begin_quiz'),
    path('quiz/', quiz, name='quiz'),
    path('results/', results, name='results'),
]
