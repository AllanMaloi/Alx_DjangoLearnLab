# Generated by Django 5.1.5 on 2025-02-22 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0004_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_add_special_book', 'Can add special book'), ('can_change_special_book', 'Can change special book'), ('can_delete_special_book', 'Can delete special book')]},
        ),
    ]
