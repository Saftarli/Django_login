# Generated by Django 5.1.5 on 2025-01-30 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_publisher_year_book_published_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reader',
            old_name='mail',
            new_name='email',
        ),
    ]
