from django.apps import AppConfig


class QuestionGeneratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'question_generator'
    def ready(self):
        pass
         # Perform any initialization tasks or register signals here pass