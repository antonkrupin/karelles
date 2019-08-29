from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail

from .models import Contacts, price_300,price_301,price_citizen,Contact,Photos

def index(request):
    contacts = Contacts.objects.all()
    prices_300 = price_300.objects.all()
    prices_301 = price_301.objects.all()
    prices_citizen = price_citizen.objects.all()
    phts = Photos.objects.all()

    context = {
        'contacts': contacts,
        'prices_300': prices_300,
        'prices_301': prices_301,
        'prices_citizen': prices_citizen,
        'phts':phts,
    }
    
    return render(request, 'base.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        dztype = request.POST['check_type']

        contact_save = Contact(name=name, phone=phone, email=email, dztype=dztype)

        contact_save.save()

        send_mail(
            'Запрос на получение материалов дистанционного зондирования',
            'Имя: ' + name + '\nТелефон: ' + phone +'\nЭлектронная почта: '+ email + '\nТип нужных материалов ДЗ: ' + dztype,
            'krupin_anton@mail.ru',
            ['krupin_anton@mail.ru','krupinanton87@gmail.com']
        )
    return redirect('index')
