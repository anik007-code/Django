# Generated by Django 4.2.16 on 2024-11-01 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('icon_class', models.CharField(default='ti-vector', max_length=50)),
                ('short_description', models.TextField()),
                ('detailed_description', models.TextField()),
            ],
        ),
    ]
