from django.db import models

class Gadget_HW(models.Model):
    id_HW = models.IntegerField(db_column='idGadget', primary_key=True)
    name = models.CharField(db_column='PIB', max_length=70)
    adress = models.CharField(db_column='Adress', max_length=70)

    # class Meta:
    #     app_label = 'plm_db'

class Meter(models.Model):
    gadget_HW = models.ForeignKey('Gadget_HW', blank=True, null=True, default=None, on_delete=models.CASCADE)  # Field name made lowercase.
    kWh = models.FloatField(db_column='kWh', blank=True, null=True)
    kvarh_p = models.FloatField(db_column='kVArh_p', blank=True, null=True)  # Field name made lowercase.
    kvarh_n = models.FloatField(db_column='kVArh_n', blank=True, null=True)  # Field name made lowercase.
    kvah = models.FloatField(db_column='kVAh', blank=True, null=True)  # Field name made lowercase.
    cur_sum_v = models.FloatField(db_column='cur_sum_V', blank=True, null=True)  # Field name made lowercase.
    cur_l1_v = models.FloatField(db_column='cur_L1_V', blank=True, null=True)  # Field name made lowercase.
    cur_l2_v = models.FloatField(db_column='cur_L2_V', blank=True, null=True)  # Field name made lowercase.
    cur_l3_v = models.FloatField(db_column='cur_L3_V', blank=True, null=True)  # Field name made lowercase.
    cur_f = models.FloatField(db_column='cur_F', blank=True, null=True)  # Field name made lowercase.
    meterDate = models.BigIntegerField(db_column='meterDate')

    # class Meta:
    #     app_label = 'plm_db'


class Meter_max_dem_h(models.Model):
    gadget_HW = models.ForeignKey('Gadget_HW', blank=True, null=True, default=None, on_delete=models.CASCADE)  # Field name made lowercase.
    kW = models.FloatField(db_column='kW', blank=True, null=True)
    meterDate = models.DateField()

    # class Meta:
    #     app_label = 'plm_db'

