# Generated by Django 3.1.5 on 2021-01-15 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210115_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='country',
        ),
    ]
