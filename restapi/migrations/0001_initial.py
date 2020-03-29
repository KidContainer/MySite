# Generated by Django 2.2.4 on 2020-03-29 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Record Date')),
                ('AAT', models.IntegerField(verbose_name='AAT Number')),
                ('essay', models.IntegerField(verbose_name='Essay Number')),
                ('other', models.IntegerField(verbose_name='Other Number')),
                ('coding', models.IntegerField(verbose_name='Coding Number')),
                ('note', models.CharField(default='', max_length=140, verbose_name='Note')),
                ('token', models.CharField(default='', max_length=100, verbose_name='Token')),
            ],
        ),
    ]
