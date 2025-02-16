# Generated by Django 4.2.5 on 2025-02-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0003_eventuserregistration_rsvp_notes_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventuserregistration",
            name="status",
            field=models.CharField(
                choices=[
                    ("rsvped", "Rsvped"),
                    ("waitlisted", "Waitlisted"),
                    ("cancelled", "Cancelled"),
                    ("attended", "Attended"),
                ],
                max_length=50,
            ),
        ),
    ]
