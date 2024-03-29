# Generated by Django 4.2.11 on 2024-03-29 09:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManagementSystem', '0019_alter_librarycard_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarycard',
            name='expiration_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='librarycard',
            name='issued_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
