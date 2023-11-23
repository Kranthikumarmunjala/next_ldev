# Generated by Django 4.2.7 on 2023-11-15 12:07

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', djrichtextfield.models.RichTextField()),
                ('description', djrichtextfield.models.RichTextField()),
            ],
        ),
    ]