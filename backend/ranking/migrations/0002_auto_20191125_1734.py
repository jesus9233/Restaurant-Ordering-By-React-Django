# Generated by Django 2.2.7 on 2019-11-25 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='recommend',
            unique_together={('username', 'chickenID')},
        ),
    ]
