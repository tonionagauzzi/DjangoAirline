# Generated by Django 3.2.3 on 2021-05-28 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20210527_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight')),
            ],
        ),
    ]
