# Generated by Django 2.2.7 on 2019-12-02 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20191202_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuinfo',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
