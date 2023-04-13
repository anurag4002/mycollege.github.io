from django.contrib import admin

# Register your models here.
from .models import *


class contactAdmin(admin.ModelAdmin):
    list_display=('name','email','mobile','message')


admin.site.register(contact,contactAdmin)



class galleryAdmin(admin.ModelAdmin):
    list_display=('id','pdes','gpic','gdate')

admin.site.register(gallery,galleryAdmin)


class recuitersAdmin(admin.ModelAdmin):
    list_display=('name','rpic','rdate')

admin.site.register(recuiters,recuitersAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=('cname','cpic','cdate')

admin.site.register(category,categoryAdmin)


class coursesAdmin(admin.ModelAdmin):
    list_display = ('cname', 'cpic', 'cdate')

admin.site.register(courses,coursesAdmin)


class placementsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'pcourse', 'branch','cmpname','cmplogo','city','pyear','designation','stupic','pdate')

admin.site.register(placements,placementsAdmin)






