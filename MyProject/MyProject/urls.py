
from django.contrib import admin
from django.urls import path,include

admin.site.site_header="Anurag mishra Admin"
admin.site.site_title="My College admin portal"
admin.site.index_title="Welcome to My College Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('',include('user.urls')),
]
