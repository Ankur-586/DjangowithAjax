# Generated by Django 4.2.11 on 2024-03-10 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManagementSystem', '0004_book_quantity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Loan',
            new_name='Borrower',
        ),
    ]
