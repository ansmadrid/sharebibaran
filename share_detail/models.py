from django.db import models

class Share(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    quantity = models.IntegerField(default=100,blank=False, null=False)
    bought_rate = models.DecimalField(max_digits=10, decimal_places=2,blank=False, null=False )
    bought_date = models.DateField(blank=True, null=True)
    sale_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_date = models.DateField(blank=True, null=True)
    today_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    sold = models.BooleanField(blank=True, null=True)
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)

