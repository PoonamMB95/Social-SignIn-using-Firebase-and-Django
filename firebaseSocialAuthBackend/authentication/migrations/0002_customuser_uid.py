# Generated by Django 3.2.4 on 2021-07-13 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='uid',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
