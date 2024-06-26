# Generated by Django 5.0.4 on 2024-04-20 20:07
from os.path import exists

from django.db import migrations
import os
import csv
from datetime import datetime
from django.core.files import File
from django.conf import settings
from semlor.models import City, Bakery, Semlor


def create_models_from_csv(apps, schema_editor):
    file_path = os.path.join(settings.BASE_DIR, "initial_data", "semlor.csv")
    with open(file_path, newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            city, created = City.objects.get_or_create(name=row["City"])

            bakery, created = Bakery.objects.get_or_create(
                name=row["Bakery"],
                city=city,
                address=row["City"],  # Dummy
                lat=0,
                long=0,
            )

            semlor = Semlor.objects.create(
                bakery=bakery,
                is_vegan=(row["Vegan"] == "T"),
                semlor_type=row["Kind"],
                price=float(row["Price"].replace(",", ".")),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )

            if row["Picture"]:
                picture_path = os.path.join(
                    settings.BASE_DIR, "initial_data", row["Picture"]
                )
                if exists(picture_path):
                    with open(picture_path, "rb") as f:
                        semlor.picture.save(row["Picture"], File(f))


class Migration(migrations.Migration):

    dependencies = [
        ("semlor", "0001_initial"),
    ]

    operations = [migrations.RunPython(create_models_from_csv)]
