# Generated by Django 5.0.7 on 2024-08-08 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'todo_item', 'verbose_name_plural': 'todo_items'},
        ),
        migrations.AlterModelTable(
            name='todo',
            table='todos',
        ),
    ]
