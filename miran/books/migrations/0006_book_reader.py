# Generated by Django 4.2.5 on 2023-10-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_history_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='reader',
            field=models.CharField(default='', max_length=100),
        ),
    ]