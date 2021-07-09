# Generated by Django 3.1.4 on 2020-12-31 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frus', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=50)),
                ('issue', models.TextField(max_length=200)),
                ('counsellor', models.CharField(max_length=50)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]