from __future__ import unicode_literals

from django.db import models
from datetime import date

import uuid

from team.models import Team

class Transaction(models.Model):
    """
    id, team, details, type, amount
    """
    
    DEBIT = 'D'
    CREDIT = 'C'
    
    TRANSACTION_TYPE = (
        (DEBIT, 'Debit'),
        (CREDIT, 'Credit'),
    )
    
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
    team = models.ForeignKey(Team)
    detail = models.CharField(max_length=256, blank=True, null=True)
    
    transaction_type = models.CharField(max_length=2,
                                      choices=TRANSACTION_TYPE,
                                      default=DEBIT)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    
    transaction_date = models.DateField(blank=False, null=False)
    
    class Meta:
        db_table = 'transaction'
        ordering = ['-transaction_date']
        
    def __unicode__(self):
        return self.details


