# Generated by Django 4.0.5 on 2022-07-21 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_user_role'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserInfo',
        ),
        migrations.AlterModelTable(
            name='userinfo',
            table='UserInfo',
        ),
    ]
