# Generated by Django 4.2.5 on 2023-10-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='books/')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('CLOSE', 'Close')], default='OPEN', max_length=5)),
            ],
        ),
    ]
