# Generated by Django 5.1.1 on 2024-09-29 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_rtchat', '0006_alter_groupmessage_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatgroup',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='chatgroup',
            name='groupchat_name',
        ),
        migrations.RemoveField(
            model_name='chatgroup',
            name='is_private',
        ),
        migrations.RemoveField(
            model_name='chatgroup',
            name='members',
        ),
        migrations.RemoveField(
            model_name='chatgroup',
            name='users_online',
        ),
        migrations.RemoveField(
            model_name='groupmessage',
            name='file',
        ),
    ]
