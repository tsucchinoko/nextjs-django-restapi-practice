from django.contrib import admin
from .models import Task, Post

# Register your models here.
# 管理画面で見れるようにする
admin.site.register(Post)
admin.site.register(Task)
