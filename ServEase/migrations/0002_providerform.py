# Generated by Django 4.2.7 on 2024-02-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServEase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
