# Generated by Django 5.2 on 2025-04-04 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='is_available',
            new_name='available',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='image',
        ),
        migrations.AddField(
            model_name='room',
            name='room_number',
            field=models.CharField(default=101, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotel',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='booking.hotel'),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(max_length=50),
        ),
    ]
