# Generated by Django 3.0.6 on 2020-06-06 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200601_1826'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Can mark returned'), ('can_renew', 'Can change due back date'))},
        ),
    ]
