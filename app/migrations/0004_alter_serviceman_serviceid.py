# Generated by Django 4.2.13 on 2024-05-15 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_serviceman_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceman',
            name='serviceId',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.services'),
        ),
    ]
