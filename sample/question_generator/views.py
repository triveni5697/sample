from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from question_generator.models import Question

def generate_question(request):
    question = Question.objects.order_by('?').first()
    options = question.get_random_options()
    context = {'question': question, 'options': options}
    return render(request, 'questions/question.html', context)

# Create your views here.
