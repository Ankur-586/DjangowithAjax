# Generated by Django 4.2.11 on 2024-03-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManagementSystem', '0009_alter_borrower_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_information',
            name='Penalty',
            field=models.CharField(default='No Penalty', max_length=15),
        ),
    ]
