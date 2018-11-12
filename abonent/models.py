
from django.db import models

class Abonent(models.Model):
    osrah = models.IntegerField(db_column='Osrah', primary_key=True)
    pib = models.CharField(db_column='PIB', max_length=70)
    adress = models.CharField(db_column='Adress', max_length=70)
    meter = models.IntegerField(db_column='Meter')
    date = models.DateField(default=0,blank=True, null=True)


class Oplata(models.Model):
    abonent = models.ForeignKey('Abonent', blank=True, null=True, default=None,on_delete=models.CASCADE)
    idoplata = models.AutoField(primary_key=True)
    from_date = models.DateField(default=0)
    saldo = models.FloatField()
    annotation = models.CharField(max_length=45, default=0)
    dateOpl = models.CharField(default=0, max_length=45)

class Rahunok(models.Model):
    abonent = models.ForeignKey('Abonent', blank=True, null=True, default=None,on_delete=models.CASCADE)
    idrahunok = models.AutoField(db_column='idRahunok', primary_key=True)
    datarah = models.DateField(db_column='dataRah')
    pokaz1 = models.FloatField()
    pokaz2 = models.FloatField()
    spozkwt = models.FloatField(db_column='SpozKWT')
    spozuah = models.FloatField(db_column='SpozUAH')











