# Generated by Django 2.2.2 on 2019-06-20 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devops', '0002_auto_20190620_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browerinfo',
            name='useragent',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='用户浏览器agent信息'),
        ),
    ]