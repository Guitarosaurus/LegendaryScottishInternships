# Generated by Django 2.2.28 on 2025-03-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legendary', '0003_auto_20250323_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='static/images/generic_profile.jpg', upload_to='profile_images'),
        ),
    ]
