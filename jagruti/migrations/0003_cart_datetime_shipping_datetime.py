# Generated by Django 4.2.4 on 2023-09-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jagruti', '0002_shipping'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='datetime',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='datetime',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]
