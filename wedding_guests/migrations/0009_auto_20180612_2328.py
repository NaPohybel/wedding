# Generated by Django 2.0.4 on 2018-06-12 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_guests', '0008_page_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Zdjęcie'),
        ),
    ]