# Generated by Django 3.1.1 on 2021-01-12 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_orm_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='ename',
            new_name='e_name',
        ),
    ]