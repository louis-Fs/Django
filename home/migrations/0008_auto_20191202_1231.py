# Generated by Django 2.2.7 on 2019-12-02 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191202_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scuinfo_content',
            old_name='date',
            new_name='date_1',
        ),
        migrations.RenameField(
            model_name='scuinfo_content',
            old_name='href',
            new_name='href_1',
        ),
        migrations.RenameField(
            model_name='scuinfo_content',
            old_name='tit',
            new_name='tit_1',
        ),
    ]
