# Generated by Django 4.2.16 on 2024-09-29 13:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("movies_app", "0003_platform_movie_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="created_at",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
