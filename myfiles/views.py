from django.db.models import Q
from django.shortcuts import render
from myfiles.models import *
# Create your views here.
def index(malumot):
    if 'matn' in malumot.POST:
        matn = malumot.POST.get('matn')
        matn =str(matn).strip()
        qidirish = Q(nomi__contains=matn)| Q(tur__nomi__contains=matn)
        portfolio = Portfolio.objects.filter(qidirish)
        turlar = Type.objects.all()
        team = Team.objects.all()
        return render(malumot, 'index.html', {"kalit": portfolio, "turlar": turlar, "team": team})


    elif 'subject' in malumot.POST:
        ism = malumot.POST.get('name')
        mail = malumot.POST.get('email')
        fan = malumot.POST.get('subject')
        xabar = malumot.POST.get('message')
        Message(name=ism,mail=mail,subject=fan,message=xabar).save()
    portfolio = Portfolio.objects.all()
    turlar = Type.objects.all()
    team = Team.objects.all()
    return render(malumot,'index.html',{"kalit":portfolio,"turlar":turlar, "team":team})

def filter_index(malumot,id):
    turlar = Type.objects.all()
    portfolio = Portfolio.objects.filter(tur_id=id)
    print(portfolio)
    return render(malumot,'index.html',{"kalit":portfolio,"turlar":turlar})

def team_index(malumot):
    team = Team.objects.all()
    return render(malumot,'index.html',)

