# Generated by Django 4.1.7 on 2023-03-14 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='completed',
            new_name='is_completed',
        ),
    ]