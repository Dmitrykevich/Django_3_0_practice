# Generated by Django 4.1.5 on 2023-01-17 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rubric_subrubricmanager_superrubricmanager_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubRubricManager',
        ),
        migrations.DeleteModel(
            name='SuperRubricManager',
        ),
    ]