# Generated by Django 3.1.7 on 2021-03-29 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0015_auto_20210329_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitecustomfield',
            old_name='checkbox_value',
            new_name='bool_value',
        ),
        migrations.AddField(
            model_name='sitecustomfield',
            name='string_value',
            field=models.TextField(blank=True, null=True),
        ),
    ]
