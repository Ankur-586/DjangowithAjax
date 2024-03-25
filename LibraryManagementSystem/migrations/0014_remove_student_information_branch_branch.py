# Generated by Django 4.2.11 on 2024-03-23 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LibraryManagementSystem', '0013_remove_borrower_book_borrower_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_information',
            name='branch',
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.PositiveSmallIntegerField(choices=[(1, 'No Default'), (2, 'Information Technology'), (3, 'Computer Science'), (4, 'Machenical Engineering'), (5, 'Electrical Engineering')], default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]