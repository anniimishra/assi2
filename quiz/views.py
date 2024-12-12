from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer
import random

class StartQuizView(APIView):
    def get(self, request):
        # Initialize the session
        request.session['total_questions'] = 0
        request.session['correct_answers'] = 0
        request.session['incorrect_answers'] = 0
        return Response({"message": "Quiz session started"}, status=status.HTTP_200_OK)


class GetQuestionView(APIView):
    def get(self, request):
        # Get a random question
        question = random.choice(Question.objects.all())
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubmitAnswerView(APIView):
    def post(self, request):
        # Get data from request
        question_id = request.data.get("question_id")
        selected_option = request.data.get("selected_option")

        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return Response({"error": "Invalid question ID"}, status=status.HTTP_400_BAD_REQUEST)

        # Update session data
        request.session['total_questions'] += 1
        if question.correct_option == int(selected_option):
            request.session['correct_answers'] += 1
            result = "correct"
        else:
            request.session['incorrect_answers'] += 1
            result = "incorrect"

        # Save session
        request.session.modified = True
        return Response({"result": result}, status=status.HTTP_200_OK)


class QuizStatsView(APIView):
    def get(self, request):
        stats = {
            "total_questions": request.session.get('total_questions', 0),
            "correct_answers": request.session.get('correct_answers', 0),
            "incorrect_answers": request.session.get('incorrect_answers', 0),
        }
        return Response(stats, status=status.HTTP_200_OK)

