from django import forms
from django.utils import timezone
from .models import Customers, Books, Loans
import datetime
from django.core import validators

class NewCustomerForm(forms.ModelForm):
    cust_id = forms.IntegerField(label='Customer ID', validators=[validators.MinValueValidator(200000000)])
    full_name = forms.CharField(label='Full Name', max_length=30)
    address = forms.CharField(label='Address', max_length=50)
    age = forms.IntegerField(label='Age',validators=[validators.MinValueValidator(18), validators.MaxValueValidator(99)])

    class Meta:
        model = Customers
        fields = ['cust_id', 'full_name', 'address', 'age']

class NewBookForm(forms.ModelForm):
    book_id = forms.IntegerField(label='Book ID', validators=[validators.MinValueValidator(0)])
    book_name = forms.CharField(label='Book Name', max_length=30)
    author_name = forms.CharField(label='Author Name', max_length=30)
    pub_date = forms.DateTimeField(label='Published Date', initial=timezone.now(), widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime'}))
    amount = forms.IntegerField(label='Amount', validators=[validators.MinValueValidator(0)])
    book_type = forms.IntegerField(label='Book Type', validators=[validators.MinValueValidator(1), validators.MaxValueValidator(3)])

    class Meta:
        model = Books
        fields = ['book_id', 'book_name', 'author_name', 'pub_date', 'amount', 'book_type']

class NewLoanForm(forms.ModelForm):
    cust_id = forms.IntegerField(label='Customer ID', validators=[validators.MinValueValidator(200000000)])
    book_id = forms.IntegerField(label='Book ID', validators=[validators.MinValueValidator(0)])
    loan_date = forms.DateTimeField(label='Loan Date', initial=timezone.now(), widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime'}))
    return_date = forms.DateTimeField(label='Return Date', initial=timezone.now(), widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime'}))

    class Meta:
        model = Loans
        fields = ['cust_id', 'book_id', 'loan_date', 'return_date']