from django.db.models import Sum
from django.http import HttpResponseNotFound
from django.shortcuts import render,HttpResponseRedirect
from abonent.models import Abonent
from django.urls import reverse


def abonent_list(request):
    abonent = Abonent.objects.all()
    context ={'abonent': abonent}
    return render(request, 'abonent/abonents.html', context)


def person_detail(request, person):
    pers = Abonent.objects.get(osrah=person)
    pib = pers.pib
    adress = pers.adress
    balans = pers.oplata_set.aggregate(sum=Sum('saldo'))
    annotation = pers.oplata_set.values_list('annotation',flat=True). order_by('-idoplata')
    saldo = pers.oplata_set.values_list('saldo', flat=True).order_by('-idoplata')
    date = pers.oplata_set.values_list('from_date', flat=True).order_by('-idoplata')
    date_oplata = pers.oplata_set.values_list('dateOpl', flat=True). order_by('-idoplata')

    date_pokaz = pers.rahunok_set.values_list('datarah', flat=True).order_by('-datarah')
    pokaz1 = pers.rahunok_set.values_list('pokaz1', flat=True).order_by('-datarah')
    pokaz2 = pers.rahunok_set.values_list('pokaz2', flat=True).order_by('-datarah')
    spozKWT = pers.rahunok_set.values_list('spozkwt', flat=True).order_by('-datarah')
    spozUAH = pers.rahunok_set.values_list('spozuah', flat=True).order_by('-datarah')


    zip_list1 = zip( date, saldo, annotation,date_oplata)
    zip_list2 = zip(date_pokaz, pokaz1, pokaz2, spozKWT, spozUAH)

    ctx = { 'pib': pib,
            'saldo': saldo,
            'adress':adress,
             'date': date,
            'balans': balans,
            'annotation': annotation,
            'date_opl': date_oplata,
            'zip_list1': zip_list1,
            'zip_list2': zip_list2,

           }


    return render(request, 'abonent/persons.html', ctx )



def add_abonent(request):
    if request.POST:
        abonent= Abonent(pib=request.POST.get('pib'),
                         adress=request.POST.get('adress'),
                         osrah=request.POST.get('osrah'),
                         meter=request.POST.get('meter'),
                         date=request.POST.get('date'))
        abonent.save()

        return  HttpResponseRedirect(reverse('abonent_list'))

    return render(request, 'abonent/add_abonent.html')



