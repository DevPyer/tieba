from django.db import models

# Create your models here.
from django.db import models
from DjangoUeditor.models import UEditorField #富文本使用

#用户表
class User(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='用户名')
    sex = models.BooleanField(verbose_name='性别')
    head_port = models.ImageField(verbose_name='头像',
                                  upload_to='post/images',
                                  null=True,
                                  blank=True)
    phone = models.IntegerField(null=True,
                                verbose_name='手机号')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 't_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

#帖子表
class Post(models.Model):

    name = models.CharField(max_length=50,
                            verbose_name='帖子名')
    post_time = models.DateTimeField(verbose_name='发帖时间',
                                     auto_now_add=True)
    post_info = UEditorField(verbose_name='帖子内容',
                             width=640,height=480,
                             imagePath='post/u_images/',
                             filePath='post/u_files/',
                             toolbars='full',
                             blank=True)
    the_poster = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   verbose_name='帖子作者')
    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_post'
        verbose_name = '帖子表'
        verbose_name_plural = verbose_name








