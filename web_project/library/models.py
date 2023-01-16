import datetime
from django.forms import widgets, DateField
from django.db import models
from django.utils import timezone

# Create your models here.

class Customers(models.Model):
    cust_id = models.IntegerField(default=0)
    full_name = models.CharField(max_length=30, default='none')
    address = models.CharField(max_length=50, default='none')
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name
        return self.address

class Books(models.Model):
    book_id = models.IntegerField(default=0)
    book_name = models.CharField(max_length=30, default='none')
    author_name = models.CharField(max_length=30, default='none')
    pub_date = models.DateTimeField('date published')
    amount = models.IntegerField(default=0)
    book_type = models.IntegerField(default=0)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.book_name
        return self.author_name

class Loans(models.Model):
    cust_id = models.IntegerField(default=0)
    book_id = models.IntegerField(default=0)
    loan_date = models.DateTimeField('date loan')
    return_date = models.DateTimeField('date return')
