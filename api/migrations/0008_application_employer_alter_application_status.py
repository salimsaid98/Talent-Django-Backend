# Generated by Django 4.1.7 on 2023-04-08 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_application_delete_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='employer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.employer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('applied', 'Applied'), ('rejected', 'Rejected'), ('confirm', 'confirm')], default='applied', max_length=20),
        ),
    ]
