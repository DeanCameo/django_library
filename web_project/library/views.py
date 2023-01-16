from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customers, Books, Loans
from .forms import NewCustomerForm, NewBookForm, NewLoanForm
from django.urls import reverse

# Create your views here.


def home(request):
    return HttpResponse("Welcome To The D BEST Library!")

# ----------------------------- Books ----------------------------- 

def avb_books(request):
    latest_books_list = Books.objects.order_by('-pub_date')
    context = {'latest_books_list': latest_books_list}
    return render(request, 'library/books.html', context)

def book_detail(request):
    book_detail_list = Books.objects.order_by('-book_id')
    context = {'book_detail_list': book_detail_list}
    return render(request, 'library/book_detail.html', context)

def add_book(request):
    form = NewBookForm()
    return render(request, 'library/add_book.html', {'form': form})

def new_b(request):
    form = NewBookForm(request.POST)

    if form.is_valid():
        book_id = form.cleaned_data['book_id']
        book_name = form.cleaned_data['book_name']
        author_name = form.cleaned_data['author_name']
        pub_date = form.cleaned_data['pub_date']
        amount = form.cleaned_data['amount']
        book_type = form.cleaned_data['book_type']
        Books.objects.create(book_id=book_id, book_name=book_name, author_name=author_name, pub_date=pub_date, amount=amount, book_type=book_type)
        return HttpResponseRedirect('http://127.0.0.1:8000/library/')
    else:
        msg = 'Oops, Check Yourself ):'
        form = NewBookForm()
        return render(request, 'library/add_book.html',{'form':form ,'msg':msg})


# ----------------------------- Customers -----------------------------


def avb_customers(request):
    customers_list = Customers.objects.order_by('-cust_id')
    context = {'customers_list': customers_list}
    return render(request,'library/customers.html', context)

def cust_detail(request):
    detail_list = Customers.objects.order_by('-cust_id')
    context = {'detail_list': detail_list}
    return render(request, 'library/cust_detail.html', context)

def add_cust(request):
    form = NewCustomerForm()
    return render(request, 'library/add_cust.html', {'form': form})

def new_c(request):
    form = NewCustomerForm(request.POST)

    if form.is_valid():
        cust_id = form.cleaned_data['cust_id']
        full_name = form.cleaned_data['full_name']
        address = form.cleaned_data['address']
        age = form.cleaned_data['age']
        Customers.objects.create(cust_id=cust_id, full_name=full_name, address=address, age=age)
        return HttpResponseRedirect('http://127.0.0.1:8000/library/customers/')
    else:
        msg = 'Oops, Check Yourself ):'
        form = NewCustomerForm()
        return render(request, 'library/add_cust.html',{'form':form ,'msg':msg})


# ----------------------------- Loans -----------------------------


def avb_loans(request):
    loans_list = Loans.objects.order_by('-book_id')
    context = {'loans_list': loans_list}
    return render(request, 'library/loans.html', context)

def loan_detail(request):
    loan_detail_list = Loans.objects.order_by('-book_id')
    context = {'loan_detail_list': loan_detail_list}
    return render(request, 'library/loan_detail.html', context)

def add_loan(request):
    form = NewLoanForm()
    return render(request, 'library/add_loan.html', {'form': form})

def new_l(request):
    form = NewLoanForm(request.POST)

    if form.is_valid():
        cust_id = form.cleaned_data['cust_id']
        book_id = form.cleaned_data['book_id']
        loan_date = form.cleaned_data['loan_date']
        return_date = form.cleaned_data['return_date']
        Loans.objects.create(cust_id=cust_id, book_id=book_id, loan_date=loan_date, return_date=return_date)
        return HttpResponseRedirect('http://127.0.0.1:8000/library/loans/')
    else:
        msg = 'Oops, Check Yourself ):'
        form = NewLoanForm()
        return render(request, 'library/add_loan.html',{'form':form ,'msg':msg})
