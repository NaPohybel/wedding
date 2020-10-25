# Generated by Django 3.0.10 on 2020-10-25 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('attending', models.PositiveSmallIntegerField(choices=[(1, 'Yes'), (2, 'No'), (3, 'Maybe')], default=3, verbose_name='attending')),
                ('attending_afters', models.PositiveSmallIntegerField(choices=[(1, 'Yes'), (2, 'No'), (3, 'Maybe')], default=3, verbose_name='attening afters')),
                ('wants_bus', models.BooleanField(default=False, verbose_name='Wants bus')),
                ('is_vegetarian', models.BooleanField(default=False, verbose_name='is vegetarian')),
                ('comments', models.TextField(blank=True, max_length=200, verbose_name='additional comment')),
                ('is_accompanying_person', models.BooleanField(default=False, verbose_name='is accompanying person')),
                ('eligible_for_afters', models.BooleanField(default=False, verbose_name='eligible for afters')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Guest',
                'verbose_name_plural': 'Guests',
            },
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('url', models.URLField(blank=True, null=True)),
                ('guest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wedding_guests.Guest', verbose_name='guest')),
            ],
            options={
                'verbose_name': 'Gift',
                'verbose_name_plural': 'Gifts',
            },
        ),
    ]
