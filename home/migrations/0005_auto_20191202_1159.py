# Generated by Django 2.2.7 on 2019-12-02 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_stuinfo_hobby'),
    ]

    operations = [
        migrations.CreateModel(
            name='scuinfo_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.CharField(max_length=500)),
                ('tit', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='scuinfo_pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_pic_url', models.CharField(max_length=200)),
                ('left_pic_url', models.CharField(max_length=200)),
                ('left_tit_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='stuinfo',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='stuinfo',
            name='phone',
            field=models.IntegerField(max_length=20),
        ),
    ]
