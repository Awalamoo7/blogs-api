# Generated by Django 3.2.8 on 2021-10-23 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]