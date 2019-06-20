from django.db import models

# Create your models here.

#verbose_name表示表述名
class UserIPInfo(models.Model):
    ip = models.CharField(max_length=40,default='',verbose_name=u'ip地址')
    time = models.DateTimeField(verbose_name=u'更新时间',auto_now=True)
    class Meta: # 这个类定义数据库生成的表的信息
        verbose_name = u'用户访问地址信息表'
        verbose_name_plural = verbose_name
        #设置这个类model在mysql数据库的实际表名
        db_table = 'useripinfo'


class BrowerInfo(models.Model):
    useragent = models.TextField(max_length=254,default='test',verbose_name=u'agent',null=True)
    models.CharField(max_length=256,verbose_name=u'唯一设备ID',default='')
    userip = models.ForeignKey('UserIPInfo',on_delete=True)
    class Meta:
        verbose_name = u'用户浏览器信息表'
        verbose_name_plural = verbose_name
        db_table = 'browerinfo'