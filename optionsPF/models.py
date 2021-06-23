from django.db import models
from django.db.models import DateTimeField, JSONField
from django.contrib.auth.models import User
import datetime


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    id = models.BigAutoField(primary_key=True)
    strategies = JSONField()

    def return_strategies(self):
        attributes = {"strategies": self.strategies}
        return attributes


class ButterflySpread(models.Model):
    id = models.BigAutoField(primary_key=True)
    strike = models.PositiveIntegerField()
    contract_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = DateTimeField()
    expiry_date = DateTimeField()
    num_contracts = models.PositiveIntegerField()
    ticker = models.CharField(max_length=5)
    strategy_name = models.CharField(max_length=20)

    def return_attributes(self):
        attributes = {"strike": self.strike, "contract_price": self.contract_price, 'purchase_date': self.purchase_date,
                      "expiry_date": self.expiry_date, "num_contracts": self.num_contracts, "ticker": self.ticker,
                      "strategy": self.strategy_name}
        return attributes




