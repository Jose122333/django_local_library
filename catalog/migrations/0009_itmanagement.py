# Generated by Django 2.0.5 on 2018-05-30 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20180530_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='ITManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projects', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('businessProcesses', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('services', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
            options={
                'permissions': (('see_itmanagement', 'Ver la capa de gestión'),),
            },
        ),
    ]
