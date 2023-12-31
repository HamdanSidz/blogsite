# Generated by Django 4.1 on 2023-07-06 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blogapp", "0002_post_date_created_post_date_updated_post_parent_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
