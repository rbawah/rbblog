# Generated by Django 3.2.5 on 2021-10-28 19:32

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211028_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(validators=[django.core.validators.MinLengthValidator(2, 'Body must be 2 characters or more.')]),
        ),
    ]
