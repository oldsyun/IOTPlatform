# Generated by Django 2.1.2 on 2018-10-31 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='introduction',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='tel',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='token',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user_id',
        ),
    ]
