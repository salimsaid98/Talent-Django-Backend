# Generated by Django 4.1.7 on 2023-03-11 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_skills_skills_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='end_date',
            new_name='eend_date',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='start_date',
            new_name='estart_date',
        ),
        migrations.RenameField(
            model_name='work_experience',
            old_name='end_date',
            new_name='wend_date',
        ),
        migrations.RenameField(
            model_name='work_experience',
            old_name='start_date',
            new_name='wstart_date',
        ),
    ]
