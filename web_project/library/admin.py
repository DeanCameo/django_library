from django.contrib import admin
from .models import Customers, Books, Loans

# Register your models here.

admin.site.register(Customers)
admin.site.register(Books)
admin.site.register(Loans)
