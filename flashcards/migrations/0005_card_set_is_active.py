# Generated by Django 2.1.5 on 2019-09-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0004_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='card_set',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
