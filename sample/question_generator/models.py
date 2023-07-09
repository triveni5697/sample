

from django.db import models


class Question(models.Model):

    text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3= models.CharField(max_length=255)
    option4= models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)


'''
class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    text = models.CharField(max_length=255)

    is_correct = models.BooleanField(default=False)
'''