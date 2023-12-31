# Generated by Django 4.2.2 on 2023-07-08 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question_generator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='option1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option4',
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_generator.question')),
            ],
        ),
    ]
