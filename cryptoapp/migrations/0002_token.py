# Generated by Django 4.0.2 on 2022-02-16 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nazwa')),
                ('shortcut', models.CharField(max_length=6, verbose_name='Ticker')),
                ('description', models.TextField(verbose_name='Opis')),
            ],
        ),
    ]