# Generated by Django 4.2.5 on 2023-11-02 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_history_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]