# Generated by Django 2.0.6 on 2018-06-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lsgd', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='id',
        ),
        migrations.AlterField(
            model_name='district',
            name='district_code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
