# Generated by Django 2.1.7 on 2019-03-23 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shareaccount',
            name='status',
            field=models.CharField(choices=[('Deactivated', 'Deactivated'), ('Activated', 'Activated')], default='Deactivated', max_length=11),
        ),
    ]
