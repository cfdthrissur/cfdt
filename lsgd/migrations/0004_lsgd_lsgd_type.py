# Generated by Django 2.0.6 on 2018-06-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lsgd', '0003_lsgd'),
    ]

    operations = [
        migrations.AddField(
            model_name='lsgd',
            name='lsgd_type',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
