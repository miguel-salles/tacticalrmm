# Generated by Django 3.1.7 on 2021-04-15 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0007_script_args'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='guid',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]