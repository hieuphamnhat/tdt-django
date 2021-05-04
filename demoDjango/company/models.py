from django.db import models

# Create your models here.
class Company(models.Model):
    symbol = models.CharField(max_length=50)
    price = models.FloatField(null=True)
    date = models.DateField(null=True)

    def get_info(self):
        return 'Symbol: ' + self.symbol + ' price: ' + self.price + ' date: ' + self.date
    
    def __repr__(self):
        return self.symbol + ' is added.'