# Generated by Django 3.1.1 on 2020-11-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20201124_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
