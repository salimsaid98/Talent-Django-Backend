# Generated by Django 4.1.7 on 2023-03-10 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_remove_skills_skills_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal_skills',
            old_name='skills',
            new_name='skill',
        ),
    ]
