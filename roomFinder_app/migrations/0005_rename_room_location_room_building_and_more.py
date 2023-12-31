# Generated by Django 4.2.6 on 2023-11-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roomFinder_app", "0004_alter_reservation_approved"),
    ]

    operations = [
        migrations.RenameField(
            model_name="room", old_name="room_location", new_name="building",
        ),
        migrations.RemoveField(model_name="reservation", name="created_at",),
        migrations.RemoveField(model_name="room", name="capacity",),
        migrations.RemoveField(model_name="room", name="room_name",),
        migrations.AddField(
            model_name="room",
            name="room_id",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="approved",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="reservation", name="day", field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="reservation", name="end_time", field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name="reservation", name="start_time", field=models.TimeField(),
        ),
    ]
