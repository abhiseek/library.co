# Generated by Django 5.1 on 2024-10-03 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_address_alter_customuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
