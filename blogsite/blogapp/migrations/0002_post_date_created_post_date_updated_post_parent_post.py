# Generated by Django 4.1 on 2023-06-23 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="date_created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="date_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="parent_post",
            field=models.IntegerField(null=True),
        ),
    ]
