from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('course/',views.course),
    path('contactus/',views.contactus),
    #path('adminlogin/',views.adminlogin),
    path('myprofile/',views.myprofile),
    path('faculty/',views.faculty),
    path('computerscience/',views.computerscience),
    path('informationtechnology/',views.informationtechnology),
    path('mechanical/',views.mechanical),
    path('electrical/',views.electrical),
    path('gallery/',views.imagegallery),
    path('recuiters/',views.grecuiters),
    path('courses/',views.courses),
    path('placements/',views.ourplacement),

]