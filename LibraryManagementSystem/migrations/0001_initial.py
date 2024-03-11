# Generated by Django 4.2.11 on 2024-03-11 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publication_year', models.IntegerField()),
                ('isbn', models.CharField(max_length=13)),
                ('quantity', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryManagementSystem.author')),
            ],
        ),
        migrations.CreateModel(
            name='Book_Borrower_Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LibraryCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=20, unique=True)),
                ('issued_date', models.DateField(default=django.utils.timezone.now)),
                ('expiration_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryManagementSystem.book')),
                ('book_borrower_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryManagementSystem.book_borrower_student')),
            ],
        ),
        migrations.AddField(
            model_name='book_borrower_student',
            name='library_card',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='LibraryManagementSystem.librarycard'),
        ),
        migrations.AddField(
            model_name='book_borrower_student',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
