from django.db import models

# Create your models here.
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.IntegerField()  # 1, 2, 3, or 4

    def __str__(self):
        return self.question_text


class QuizSession(models.Model):
    user = models.CharField(max_length=100, default="default_user")  # Fixed user
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)

    def __str__(self):
        return f"Session for {self.user}"

