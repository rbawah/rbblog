# Generated by Django 3.2.5 on 2021-10-22 01:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('NB', 'Non-binary'), ('Z', 'Would rather not say'), ('UK', 'Unknown')], help_text='Select your gender', max_length=2, null=True)),
                ('bio', models.TextField(blank=True, help_text='Tell your readers about yourself...', max_length=1000, null=True, verbose_name='About the Writer')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('city', models.CharField(blank=True, help_text='Where do you live?', max_length=255, null=True, verbose_name='City')),
                ('phone', models.PositiveIntegerField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, help_text='Enter your LinkedIn URL here', null=True, verbose_name='LinkedIn')),
                ('twitter', models.URLField(blank=True, help_text='Enter your Twitter URL here', null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, help_text='Enter your Instagram URL here', null=True, verbose_name='Instagram')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]