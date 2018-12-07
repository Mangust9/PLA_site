
from django.db import models

class Abonent(models.Model):
    osrah = models.IntegerField(db_column='Osrah', primary_key=True)
    pib = models.CharField(db_column='PIB', max_length=70)
    adress = models.CharField(db_column='Adress', max_length=70)
    meter = models.IntegerField(db_column='Meter')
    date = models.DateField()

    # class Meta:
    #     app_label = 'abonent_db'

class Oplata(models.Model):
    abonent = models.ForeignKey('Abonent', blank=True, null=True, default=None,on_delete=models.CASCADE)
    idoplata = models.AutoField(primary_key=True)
    from_date = models.DateField()
    saldo = models.FloatField()
    annotation = models.CharField(max_length=45, default=0)
    dateOpl = models.CharField(default=None, max_length=45)

    # class Meta:
    #     app_label = 'abonent_db'

class Rahunok(models.Model):
    abonent = models.ForeignKey('Abonent', blank=True, null=True, default=None, on_delete=models.CASCADE)
    idrahunok = models.AutoField(db_column='idRahunok', primary_key=True)
    datarah = models.DateField()
    pokaz1 = models.FloatField()
    pokaz2 = models.FloatField()
    spozkwt = models.FloatField(db_column='SpozKWT')
    spozuah = models.FloatField(db_column='SpozUAH')

    # class Meta:
    #     app_label = 'abonent_db'


class Abonent_comercial(models.Model):
    name = models.CharField(db_column='Name', max_length=30)
    edrpoy = models.FloatField(db_column='EDRPOY', max_length=9, primary_key=True)
    adress = models.CharField(db_column='Adress', max_length=70)
    contrNum = models.FloatField(db_column='ContractNum', max_length=20,  primary_key=True)
    taxNum = models.FloatField(db_column='TaxNum', max_length=20,  primary_key=True)
    certificateNum = models.FloatField(db_column='CerttificateNum', max_length=32,  primary_key=True)
    phoneNum = models.FloatField(db_column='PhoneNum', max_length=20)
    date = models.DateField(db_column='DateContract', max_length=15)










