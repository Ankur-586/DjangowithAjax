# Generated by Django 4.2.11 on 2024-03-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManagementSystem', '0011_alter_student_information_penalty'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_information',
            name='branch',
            field=models.PositiveSmallIntegerField(choices=[(1, 'No Default'), (2, 'Information Technology'), (3, 'Computer Science'), (4, 'Machenical Engineering'), (5, 'Electrical Engineering')], default=1),
        ),
    ]