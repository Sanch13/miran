# Generated by Django 4.2.5 on 2023-10-24 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_reader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='reader',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
