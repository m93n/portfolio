from django.shortcuts import render
from . import models

def home(request):
    home_data = models.home_page.objects.all()
    media_data = models.media_page.objects.all()
    contact_data = models.contact.objects.all()
    about_data = models.about.objects.all()
    skill_data = models.skill.objects.all()
    workExp_data = models.workExp.objects.all()
    educationExp_data = models.educationExp.objects.all()
    rows = list(range(int(len(skill_data)/2))) if len(skill_data)/2 == 0 else list(range(int((len(skill_data)-1)/2+1)))
    data = {"home_data":home_data, "media_data":media_data,
            "contact_data":contact_data, "about_data":about_data,
            "skill_data":skill_data, "workExp_data":workExp_data,
            "educationExp_data":educationExp_data,}
    return render(request, "Home/index.html", {"rows":rows, 'data':data})