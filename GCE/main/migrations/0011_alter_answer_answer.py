# Generated by Django 4.2.3 on 2024-01-24 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_delete_series_subject_advanced_subject_ordinary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(max_length=100000),
        ),
    ]