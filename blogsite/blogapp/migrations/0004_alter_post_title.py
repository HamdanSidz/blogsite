# Generated by Django 4.1 on 2023-07-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0003_alter_post_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
