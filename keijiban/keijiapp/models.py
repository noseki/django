from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# ユーザーアカウントのモデルクラス
class Account(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    account_image = models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username

class ThreadModel(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    created_time = models.DateTimeField(help_text="作成日", auto_now_add=True)
    updated_time = models.DateTimeField(help_text="更新日", auto_now=True)
   

    def __str__(self):
        return self.title

class ThreadModelAdmin(admin.ModelAdmin):
    list_display = ('title','content', 'created_time', 'updated_time',)
    readonly_fields = ('updated_time',)