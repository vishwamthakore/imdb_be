# Generated by Django 4.2.16 on 2024-09-29 13:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("movies_app", "0002_movie_is_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="Platform",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=200)),
                ("website", models.URLField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="movie",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
