# Generated by Django 2.0.2 on 2018-06-12 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=256)),
                ('Last_Name', models.CharField(max_length=256)),
                ('Email_Address', models.CharField(max_length=256)),
                ('Mobile_Number', models.IntegerField()),
                ('Intereset', models.TextField()),
            ],
        ),
    ]
