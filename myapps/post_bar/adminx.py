from django.contrib import admin

# Register your models here.
import xadmin
from xadmin import views
from post_bar.models import User, Post

#配置主题
class BaseSettings:
    enable_themes = False
    use_bootswatch = False

#全局的配置
class GlobalSettings:
    site_title = '贴吧管理系统'
    site_footer = '@<span style="font-size:25px; color:blue;">zero.</span> <a href="http://www.qfedu.com" class="btn btn-link">郑州Py1802</a>'
    menu_style = 'accordion' #菜单折叠效果

    globals_search_models = [User, Post]
    #样式
    global_models_icon = {
        User: 'glyphicon glyphicon-cloud',
        Post: 'glyphicon glyphicon-music'
    }

#配置模型的输出
class PostAdmin:
    list_display = ['name', 'post_time', 'the_poster']
    search_fields = ['name']

class UserAdmin(object):
    list_display = ['name', 'sex', 'phone']
    search_fields = ['name']
    list_per_page = 10
    #设置字段的样式
    style_fields = {
        'content': 'ueditor'
    }

xadmin.site.register(views.BaseAdminView,BaseSettings)
xadmin.site.register(views.CommAdminView,GlobalSettings)


xadmin.site.register(User,UserAdmin)
xadmin.site.register(Post,PostAdmin)

























