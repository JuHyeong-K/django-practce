# Generated by Django 3.2.3 on 2021-05-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='content',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.TextField(default=1622095223.4953892),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
