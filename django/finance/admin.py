from django.contrib import admin

from models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_filter = ['transaction_type', 'team' ]
    list_display = ['team','transaction_date','detail', 'transaction_type','amount']

admin.site.register(Transaction, TransactionAdmin)
