# Generated by Django 3.1.3 on 2023-08-02 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_correct',
            new_name='is_correct',
        ),
    ]