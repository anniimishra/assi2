from django.urls import path
from .views import StartQuizView, GetQuestionView, SubmitAnswerView, QuizStatsView

urlpatterns = [
    path('start/', StartQuizView.as_view(), name='start_quiz'),
    path('get-question/', GetQuestionView.as_view(), name='get_question'),
    path('submit-answer/', SubmitAnswerView.as_view(), name='submit_answer'),
    path('stats/', QuizStatsView.as_view(), name='quiz_stats'),
]
