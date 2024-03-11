# Generated by Django 5.0.3 on 2024-03-11 13:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=255, verbose_name='Descripction')),
                ('type', models.CharField(choices=[('DA', 'Data'), ('DE', 'Development'), ('AD', 'Admin')], default='DE', max_length=2, verbose_name='Type')),
                ('status', models.CharField(choices=[('OP', 'Opened'), ('CL', 'Closed'), ('AB', 'Aborted'), ('PA', 'Paused')], default='OP', max_length=2, verbose_name='Status')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('end_date', models.DateField(verbose_name='End date')),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Task',
                'order_with_respect_to': 'user',
            },
        ),
    ]