# Generated by Django 3.2.5 on 2021-11-09 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['id']},
        ),
    ]
