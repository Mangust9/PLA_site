from django.shortcuts import render

from abonent.models import Oplata


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Якщо у вас виникли запитання, то можете задати їх по '
                                                             'телефону або по електронній пошті', '(063)21-98-875', 'асрар2@gmail.com']})


