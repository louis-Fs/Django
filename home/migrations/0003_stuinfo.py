# Generated by Django 2.2.7 on 2019-12-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_stuinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='stuinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('intro', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=4)),
                ('grade', models.CharField(max_length=10)),
                ('hobby', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
