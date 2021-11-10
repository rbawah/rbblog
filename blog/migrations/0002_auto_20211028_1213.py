# Generated by Django 3.2.5 on 2021-10-28 18:13

import ckeditor.fields
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(validators=[django.core.validators.MinLengthValidator(2, 'Body must be 2 characters or more.')]),
        ),
    ]