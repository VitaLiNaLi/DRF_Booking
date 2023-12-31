# Generated by Django 4.2.2 on 2023-06-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_hotel_description_room_bed_room_description_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="hotel",
        ),
        migrations.RemoveField(
            model_name="booking",
            name="typeOfRoom",
        ),
        migrations.AlterField(
            model_name="booking",
            name="room",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="room",
            name="bed",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
