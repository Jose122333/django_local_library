# Generated by Django 2.0.5 on 2018-06-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20180602_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='itmanagement',
            name='arrow1File',
            field=models.FileField(blank=True, upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='itmanagement',
            name='arrow1Name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='itmanagement',
            name='arrow2File',
            field=models.FileField(blank=True, upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='itmanagement',
            name='arrow2Name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='itmanagement',
            name='arrow3File',
            field=models.FileField(blank=True, upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='itmanagement',
            name='arrow3Name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='itmanagement',
            name='arrow4File',
            field=models.FileField(blank=True, upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='itmanagement',
            name='arrow4Name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='itmanagement',
            name='arrow5File',
            field=models.FileField(blank=True, upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='itmanagement',
            name='arrow5Name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
