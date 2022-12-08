from django.contrib import admin
from myfiles.models import *
# Register your models here.


class AdminP(admin.ModelAdmin):
    list_display = ['id','nomi','tur','rasm']
admin.site.register(Portfolio,AdminP)


class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Type,AdminType)


class AdminTeam(admin.ModelAdmin):
    list_display = ['id','ism','martaba','rasm', 'twiter','facebook','instagram','linced']
admin.site.register(Team,AdminTeam)

class AdminM(admin.ModelAdmin):
    list_display = ['id','name','mail','subject','message','time']
admin.site.register(Message,AdminM)

