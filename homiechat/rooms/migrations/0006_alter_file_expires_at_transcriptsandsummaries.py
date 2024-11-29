# Generated by Django 4.2.3 on 2023-12-19 09:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_alter_file_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 9, 30, 2, 580334, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='TranscriptsAndSummaries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('transcript', models.JSONField(default='No Transcript Available')),
                ('summary', models.TextField(default='No Summary Available')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room')),
            ],
        ),
    ]