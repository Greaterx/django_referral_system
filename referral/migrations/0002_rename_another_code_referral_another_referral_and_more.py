# Generated by Django 4.0.2 on 2022-03-20 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referral',
            old_name='another_code',
            new_name='another_referral',
        ),
        migrations.RenameField(
            model_name='referral',
            old_name='my_code',
            new_name='my_referral',
        ),
    ]