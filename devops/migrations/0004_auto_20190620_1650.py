# Generated by Django 2.2.2 on 2019-06-20 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devops', '0003_auto_20190620_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browerinfo',
            name='useragent',
            field=models.CharField(default='test', max_length=100, null=True, verbose_name='用户浏览器agent信息'),
        ),
    ]
