# Generated by Django 5.0.5 on 2024-05-08 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionsmodel',
            name='answer_to_question',
        ),
        migrations.AlterField(
            model_name='questionsmodel',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameapp.optionsmodel'),
        ),
    ]