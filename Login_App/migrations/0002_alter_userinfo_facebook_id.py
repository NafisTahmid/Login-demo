# Generated by Django 5.1.1 on 2024-09-30 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='facebook_id',
            field=models.URLField(blank=True),
        ),
    ]
