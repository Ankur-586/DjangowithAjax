# Generated by Django 4.2.11 on 2024-03-13 11:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManagementSystem', '0007_alter_borrower_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
