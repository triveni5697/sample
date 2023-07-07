from django.db import models

# Create your models here.
from django.db import models
from django.db import models
import random


class Question(models.Model):

    class Meta:
        app_label = 'question_generator'
    text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)

    def __str__(self):
        return self.text

    def get_random_options(self):
        options = [self.option1, self.option2, self.option3, self.option4]
        random.shuffle(options)
        return options

# Create your models here.
