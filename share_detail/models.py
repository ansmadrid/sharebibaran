from django.db import models

from django.db.models import Sum
class Share(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    quantity = models.IntegerField(default=100,blank=False, null=False)
    bought_rate = models.DecimalField(max_digits=10, decimal_places=2,blank=False, null=False )
    bought_date = models.DateField(blank=True, null=True)
    sale_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_date = models.DateField(blank=True, null=True)
    today_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    sold = models.BooleanField(blank=True, null=True, default=False)
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    total_value = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.total_value = self.today_price * self.quantity
        return super().save(*args, **kwargs)

    def balance(self, *args, **kwargs):
        total = Share.objects.all().aggregate(Sum("total_value"))
        return total