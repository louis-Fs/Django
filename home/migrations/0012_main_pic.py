# Generated by Django 2.2.7 on 2019-12-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20191202_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='main_pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hre_f', models.CharField(max_length=200)),
                ('titl_e', models.CharField(max_length=200)),
                ('pic_url', models.CharField(max_length=100)),
                ('cday', models.CharField(max_length=10)),
            ],
        ),
    ]
