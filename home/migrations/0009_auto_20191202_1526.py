# Generated by Django 2.2.7 on 2019-12-02 07:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20191202_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='scuinfo_content',
            name='cday',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scuinfo_pic',
            name='cday',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]