# Generated by Django 5.0.4 on 2024-04-21 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
            ],
        ),
        migrations.CreateModel(
            name="Bakery",
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
                ("name", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("lat", models.DecimalField(decimal_places=6, max_digits=9)),
                ("long", models.DecimalField(decimal_places=6, max_digits=9)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="semlor.city",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Semlor",
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
                ("picture", models.ImageField(upload_to="semlor_pictures/")),
                ("is_vegan", models.BooleanField(default=False)),
                (
                    "semlor_type",
                    models.CharField(
                        choices=[
                            ("Classic", "Classic"),
                            ("Wrap", "Wrap"),
                            ("Coffee", "Coffee"),
                            ("Vanilla", "Vanilla"),
                        ],
                        max_length=20,
                    ),
                ),
                ("price", models.FloatField()),
                ("rating", models.FloatField(default=0)),
                ("total_ratings", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bakery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="semlor.bakery",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rating",
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
                (
                    "rating",
                    models.IntegerField(
                        choices=[
                            (1, "1"),
                            (2, "2"),
                            (3, "3"),
                            (4, "4"),
                            (5, "5"),
                        ]
                    ),
                ),
                ("comment", models.TextField(blank=True, max_length=1024)),
                ("ip_address", models.GenericIPAddressField()),
                ("user_agent", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "semlor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ratings",
                        to="semlor.semlor",
                    ),
                ),
            ],
        ),
    ]
