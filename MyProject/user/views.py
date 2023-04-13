from django.shortcuts import render
from .models import *


# Create your views here.
def home(req):
    return render(req, 'user/index.html')


def about(req):
    return render(req, 'user/about.html')


def contactus(request):
    status = False
    if request.method == 'POST':
        Name = request.POST.get("name", "")
        Email = request.POST.get("email", "")
        Mobile = request.POST.get("mobile", "")
        Message = request.POST.get("msg", "")
        x = contact(name=Name, email=Email, mobile=Mobile, message=Message)
        x.save()
        status = True

    return render(request, 'user/contactus.html', {'S': status})


def myprofile(req):
    return render(req, 'user/myprofile.html')


#def adminlogin(req):
    #return render(req, 'user/adminlogin.html')






def computerscience(req):
    return render(req, 'user/computerscience.html')

def informationtechnology(req):
    return render(req, 'user/informationtechnology.html')

def mechanical(req):
    return render(req, 'user/mechanical.html')

def electrical(req):
    return render(req, 'user/electrical.html')


def faculty(req):
    return render(req, 'user/faculty.html')

def course(req):
    cdata=courses.objects.all()
    mydict={"c":cdata}
    return render(req,'user/course.html',mydict)

def ourplacement(req):
    cdata=courses.objects.all().order_by('-id')
    a=req.GET.get('msg')
    pdata=""
    if a is None:
        pdata=placements.objects.all()
    else:
        pdata = placements.objects.all().filter(pcourse=a)


    return render(req, 'user/placements.html',{"course":cdata,"placement":pdata})


def imagegallery(req):
    gdata = gallery.objects.filter
    mydict = {"d": gdata}

    return render(req, 'user/gallery.html', mydict)

def grecuiters(req):
    # rdata = recuiters.objects.all().order_by('-id')
    rdata = recuiters.objects.filter()
    mydict = {"d": rdata}

    return render(req,'user/recuiters.html', mydict)




