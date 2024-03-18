# Generated by Django 4.2.11 on 2024-03-17 18:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0004_alter_myuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]