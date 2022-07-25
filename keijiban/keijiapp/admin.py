from django.contrib import admin
from .models import Account, ThreadModel, ThreadModelAdmin

# Register your models here.
admin.site.register(ThreadModel,  ThreadModelAdmin)
admin.site.register(Account)