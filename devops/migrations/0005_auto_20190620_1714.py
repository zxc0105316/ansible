# Generated by Django 2.2.2 on 2019-06-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devops', '0004_auto_20190620_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browerinfo',
            name='useragent',
            field=models.TextField(default='test', max_length=254, null=True, verbose_name='agent'),
        ),
    ]