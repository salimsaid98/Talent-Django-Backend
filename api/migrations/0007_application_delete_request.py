# Generated by Django 4.1.7 on 2023-04-08 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_talent_duties_and_respo_talent_qualification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('applied', 'Applied'), ('rejected', 'Rejected'), ('pending', 'pending')], default='applied', max_length=20)),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
                ('talent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.talent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'application',
            },
        ),
        migrations.DeleteModel(
            name='Request',
        ),
    ]
