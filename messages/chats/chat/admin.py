from django.contrib import admin
from .models import Message , Room
# Register your models here.
class MessageAdmin(admin.ModelAdmin):

 admin.site.register(Message)
 admin.site.register (Room)