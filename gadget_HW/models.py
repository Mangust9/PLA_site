from django.db import models

class Gadget_HW(models.Model):
    id_HW = models.IntegerField(db_column='idGadget', primary_key=True)
    name = models.CharField(db_column='PIB', max_length=70)
    adress = models.CharField(db_column='Adress', max_length=70)



class Meter(models.Model):
    gadget_HW = models.ForeignKey('Gadget_HW', blank=True, null=True, default=None, on_delete=models.CASCADE)  # Field name made lowercase.
    kvarh_p = models.FloatField(db_column='kVArh_p', blank=True, null=True)  # Field name made lowercase.
    kvarh_n = models.FloatField(db_column='kVArh_n', blank=True, null=True)  # Field name made lowercase.
    kvah = models.FloatField(db_column='kVAh', blank=True, null=True)  # Field name made lowercase.
    cur_sum_kw = models.FloatField(db_column='cur_sum_kW', blank=True, null=True)  # Field name made lowercase.
    cur_l1_kw = models.FloatField(db_column='cur_L1_kW', blank=True, null=True)  # Field name made lowercase.
    cur_l2_kw = models.FloatField(db_column='cur_L2_kW', blank=True, null=True)  # Field name made lowercase.
    cur_l3_kw = models.FloatField(db_column='cur_L3_kW', blank=True, null=True)  # Field name made lowercase.
    cur_sum_kvar_p = models.FloatField(db_column='cur_sum_kVAr_p', blank=True, null=True)  # Field name made lowercase.
    cur_l1_kvar_p = models.FloatField(db_column='cur_L1_kVAr_p', blank=True, null=True)  # Field name made lowercase.
    cur_l2_kvar_p = models.FloatField(db_column='cur_L2_kVAr_p', blank=True, null=True)  # Field name made lowercase.
    cur_l3_kvar_p = models.FloatField(db_column='cur_L3_kVAr_p', blank=True, null=True)  # Field name made lowercase.
    cur_sum_kvar_n = models.FloatField(db_column='cur_sum_kVAr_n', blank=True, null=True)  # Field name made lowercase.
    cur_l1_kvar_n = models.FloatField(db_column='cur_L1_kVAr_n', blank=True, null=True)  # Field name made lowercase.
    cur_l2_kvar_n = models.FloatField(db_column='cur_L2_kVAr_n', blank=True, null=True)  # Field name made lowercase.
    cur_l3_kvar_n = models.FloatField(db_column='cur_L3_kVAr_n', blank=True, null=True)  # Field name made lowercase.
    cur_sum_kva = models.FloatField(db_column='cur_sum_kVA', blank=True, null=True)  # Field name made lowercase.
    cur_l1_kva = models.FloatField(db_column='cur_L1_kVA', blank=True, null=True)  # Field name made lowercase.
    cur_l2_kva = models.FloatField(db_column='cur_L2_kVA', blank=True, null=True)  # Field name made lowercase.
    cur_l3_kva = models.FloatField(db_column='cur_L3_kVA', blank=True, null=True)  # Field name made lowercase.
    cur_sum_a = models.FloatField(db_column='cur_sum_A', blank=True, null=True)  # Field name made lowercase.
    cur_l1_a = models.FloatField(db_column='cur_L1_A', blank=True, null=True)  # Field name made lowercase.
    cur_l2_a = models.FloatField(db_column='cur_L2_A', blank=True, null=True)  # Field name made lowercase.
    cur_l3_a = models.FloatField(db_column='cur_L3_A', blank=True, null=True)  # Field name made lowercase.
    cur_sum_v = models.FloatField(db_column='cur_sum_V', blank=True, null=True)  # Field name made lowercase.
    cur_l1_v = models.FloatField(db_column='cur_L1_V', blank=True, null=True)  # Field name made lowercase.
    cur_l2_v = models.FloatField(db_column='cur_L2_V', blank=True, null=True)  # Field name made lowercase.
    cur_l3_v = models.FloatField(db_column='cur_L3_V', blank=True, null=True)  # Field name made lowercase.
    cur_f = models.FloatField(db_column='cur_F', blank=True, null=True)  # Field name made lowercase.



class Arduino(models.Model):
    gadget_HW = models.ForeignKey('Gadget_HW', blank=True, null=True, default=None, on_delete=models.CASCADE)
    phase1 = models.IntegerField(db_column='phase_1', blank=True, null=True, default=None)
    phase2 = models.IntegerField(db_column='phase_2', blank=True, null=True, default=None)
    phase3 = models.IntegerField(db_column='phase_3', blank=True, null=True, default=None)
    phase4 = models.IntegerField(db_column='phase_4', blank=True, null=True, default=None)
    oilLevel = models.IntegerField(db_column='oil_level', blank=True, null=True, default=None)
    temperature = models.IntegerField(db_column='temp', blank=True, null=True, default=None)
    door = models.BooleanField(db_column='door')
    date = models.DateField(db_column='date', blank=True, null=True)
