# Generated by Django 3.2.16 on 2023-02-26 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230222_0255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('pub_date',)},
        ),
    ]
