# Generated by Django 4.1.7 on 2023-03-06 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_personal_img_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal_img',
            name='image',
        ),
    ]